# protect the default target for this file from the targets in Makefile.global
default: all

top_builddir = ..
include $(top_builddir)/src/Makefile.global

.PHONY: all install clean distclean gpcloud mapreduce

#
# targets built via top_builddir/GNUmakefile
#
recurse_targets = ""

ifeq "$(enable_debug_extensions)" "yes"
	recurse_targets = gp_sparse_vector \
               gp_distribution_policy \
               gp_internal_tools \
               gp_pitr \
               gp_debug_numsegments \
               gp_inject_fault \
               gp_replica_check \
               gp_error_handling
else
	recurse_targets = gp_sparse_vector \
               gp_distribution_policy \
               gp_internal_tools \
               gp_pitr \
               gp_error_handling
endif

ifeq "$(with_zstd)" "yes"
	recurse_targets += zstd
endif
ifeq "$(with_quicklz)" "yes"
	recurse_targets += quicklz
endif
$(call recurse,all install clean distclean, $(recurse_targets))

all: gpcloud mapreduce orafce

gpcloud:
	@if [ "$(enable_gpcloud)" = "yes" ]; then \
		$(MAKE) -C gpcloud && \
		$(MAKE) -C gpcloud/bin/gpcheckcloud; \
	fi

mapreduce:
	@if [ "$(enable_mapreduce)" = "yes" ]; then \
		$(MAKE) -C gpmapreduce; \
	fi

orafce:
	@if [ "$(enable_orafce)" = "yes" ]; then \
		$(MAKE) -C orafce NO_PGXS=true; \
	fi

install:
	@if [ "$(enable_gpcloud)" = "yes" ]; then \
		$(MAKE) -C gpcloud install && \
		$(MAKE) -C gpcloud/bin/gpcheckcloud install; \
	fi
	@if [ "$(enable_mapreduce)" = "yes" ]; then \
		$(MAKE) -C gpmapreduce install; \
	fi
	@if [ "$(enable_orafce)" = "yes" ]; then \
		$(MAKE) -C orafce NO_PGXS=true install; \
	fi

clean:
	if [ "$(enable_mapreduce)" = "yes" ]; then $(MAKE) -C gpmapreduce clean; fi
	if [ "$(enable_gpcloud)" = "yes" ]; then $(MAKE) -C gpcloud cleanall; fi
	if [ "${enable_orafce}" = "yes" ]; then $(MAKE) -C orafce NO_PGXS=true clean; fi


distclean:
	if [ "$(enable_mapreduce)" = "yes" ]; then $(MAKE) -C gpmapreduce distclean; fi
	if [ "$(enable_gpcloud)" = "yes" ]; then $(MAKE) -C gpcloud distclean; fi
	if [ "${enable_orafce}" = "yes" ]; then $(MAKE) -C orafce NO_PGXS=true distclean; fi

installcheck:
	$(MAKE) -C gp_internal_tools installcheck
	if [ "$(enable_mapreduce)" = "yes" ]; then \
		$(MAKE) -C gpmapreduce installcheck; \
	fi
	if [ "$(enable_orafce)" = "yes" ]; then $(MAKE) -C orafce installcheck; fi

ifeq "$(with_zstd)" "yes"
	$(MAKE) -C zstd installcheck
endif

ifeq "$(with_quicklz)" "yes"
	$(MAKE) -C quicklz installcheck
endif
