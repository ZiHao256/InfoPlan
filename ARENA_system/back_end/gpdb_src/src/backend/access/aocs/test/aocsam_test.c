#include <stdarg.h>
#include <stddef.h>
#include <setjmp.h>
#include "cmockery.h"

#include "postgres.h"
#include "utils/memutils.h"

#include "../aocsam.c"

/*
 * aocs_begin_headerscan()
 *
 * Verify that we are setting correct storage attributes (no
 * compression, no checksum) for scanning an existing column in ALTER
 * TABLE ADD COLUMN case.
 */
static void
test__aocs_begin_headerscan(void **state)
{
	AOCSHeaderScanDesc desc;
	RelationData reldata;
	FormData_pg_appendonly pgappendonly;

	pgappendonly.checksum = true;
	reldata.rd_appendonly = &pgappendonly;
	FormData_pg_class pgclass;

	reldata.rd_rel = &pgclass;
	StdRdOptions opt;

	opt.blocksize = 8192 * 5;
	StdRdOptions *opts[1];

	opts[0] = &opt;

	strncpy(&pgclass.relname.data[0], "mock_relation", 13);
	expect_value(RelationGetAttributeOptions, rel, &reldata);
	will_return(RelationGetAttributeOptions, &opts);

	/*
	 * We used to mock AppendOnlyStorageRead_Init() here, however as the mocked
	 * one does not initialize desc->ao_read.storageAttributes at all, it makes
	 * the following assertion flaky.
	 *
	 * On the other hand aocs_begin_headerscan() itself does not do many useful
	 * things, the actual job is done inside AppendOnlyStorageRead_Init(), so
	 * to make the test more useful we removed the mocking and test against the
	 * real AppendOnlyStorageRead_Init() now.
	 */
	desc = aocs_begin_headerscan(&reldata, 0);
	assert_false(desc->ao_read.storageAttributes.compress);
	assert_int_equal(desc->colno, 0);
}


static void
test__aocs_addcol_init(void **state)
{
	AOCSAddColumnDesc desc;
	RelationData reldata;
	FormData_pg_appendonly pgappendonly;
	int			nattr = 5;
	StdRdOptions **opts =
	(StdRdOptions **) malloc(sizeof(StdRdOptions *) * nattr);

	/* 3 existing columns */
	opts[0] = opts[1] = opts[2] = (StdRdOptions *) NULL;

	/* 2 newly added columns */
	opts[3] = (StdRdOptions *) malloc(sizeof(StdRdOptions));
	strcpy(opts[3]->compresstype, "rle_type");
	opts[3]->compresslevel = 2;
	opts[3]->blocksize = 8192;
	opts[4] = (StdRdOptions *) malloc(sizeof(StdRdOptions));
	strcpy(opts[4]->compresstype, "none");
	opts[4]->compresslevel = 0;
	opts[4]->blocksize = 8192 * 2;

	/* One call to RelationGetAttributeOptions() */
	expect_any(RelationGetAttributeOptions, rel);
	will_return(RelationGetAttributeOptions, opts);

	/* Two calls to create_datumstreamwrite() */
	expect_string(create_datumstreamwrite, compName, "rle_type");
	expect_string(create_datumstreamwrite, compName, "none");
	expect_value(create_datumstreamwrite, compLevel, 2);
	expect_value(create_datumstreamwrite, compLevel, 0);
	expect_value_count(create_datumstreamwrite, checksum, true, 2);
	expect_value_count(create_datumstreamwrite, safeFSWriteSize, 0, 2);
	expect_value(create_datumstreamwrite, maxsz, 8192);
	expect_value(create_datumstreamwrite, maxsz, 8192 * 2);
	expect_value(create_datumstreamwrite, needsWAL, true);
	expect_value(create_datumstreamwrite, needsWAL, true);
	expect_any_count(create_datumstreamwrite, attr, 2);
	expect_any_count(create_datumstreamwrite, relname, 2);
	expect_any_count(create_datumstreamwrite, title, 2);
	will_return_count(create_datumstreamwrite, NULL, 2);

	pgappendonly.checksum = true;
	FormData_pg_class rel;
	rel.relpersistence = RELPERSISTENCE_PERMANENT;
	reldata.rd_rel = &rel;
	reldata.rd_appendonly = &pgappendonly;
	reldata.rd_att = (TupleDesc) malloc(sizeof(struct tupleDesc));
	reldata.rd_att->attrs =
		(Form_pg_attribute *) malloc(sizeof(Form_pg_attribute *) * nattr);
	memset(reldata.rd_att->attrs, 0, sizeof(Form_pg_attribute *) * nattr);
	reldata.rd_att->natts = 5;
	/* 3 existing columns, 2 new columns */
	desc = aocs_addcol_init(&reldata, 2);
	assert_int_equal(desc->num_newcols, 2);
	assert_int_equal(desc->cur_segno, -1);
}

int
main(int argc, char *argv[])
{
	cmockery_parse_arguments(argc, argv);

	const		UnitTest tests[] = {
		unit_test(test__aocs_begin_headerscan),
		unit_test(test__aocs_addcol_init)
	};

	MemoryContextInit();

	return run_tests(tests);
}