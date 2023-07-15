/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_BASE_YY_GRAM_H_INCLUDED
# define YY_BASE_YY_GRAM_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int base_yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    IDENT = 258,
    FCONST = 259,
    SCONST = 260,
    BCONST = 261,
    XCONST = 262,
    Op = 263,
    ICONST = 264,
    PARAM = 265,
    TYPECAST = 266,
    DOT_DOT = 267,
    COLON_EQUALS = 268,
    ABORT_P = 269,
    ABSOLUTE_P = 270,
    ACCESS = 271,
    ACTION = 272,
    ADD_P = 273,
    ADMIN = 274,
    AFTER = 275,
    AGGREGATE = 276,
    ALL = 277,
    ALSO = 278,
    ALTER = 279,
    ALWAYS = 280,
    ANALYSE = 281,
    ANALYZE = 282,
    AND = 283,
    ANY = 284,
    ARRAY = 285,
    AS = 286,
    ASC = 287,
    ASSERTION = 288,
    ASSIGNMENT = 289,
    ASYMMETRIC = 290,
    AT = 291,
    ATTRIBUTE = 292,
    AUTHORIZATION = 293,
    BACKWARD = 294,
    BEFORE = 295,
    BEGIN_P = 296,
    BETWEEN = 297,
    BIGINT = 298,
    BINARY = 299,
    BIT = 300,
    BOOLEAN_P = 301,
    BOTH = 302,
    BY = 303,
    CACHE = 304,
    CALLED = 305,
    CASCADE = 306,
    CASCADED = 307,
    CASE = 308,
    CAST = 309,
    CATALOG_P = 310,
    CHAIN = 311,
    CHAR_P = 312,
    CHARACTER = 313,
    CHARACTERISTICS = 314,
    CHECK = 315,
    CHECKPOINT = 316,
    CLASS = 317,
    CLOSE = 318,
    CLUSTER = 319,
    COALESCE = 320,
    COLLATE = 321,
    COLLATION = 322,
    COLUMN = 323,
    COMMENT = 324,
    COMMENTS = 325,
    COMMIT = 326,
    COMMITTED = 327,
    CONCURRENCY = 328,
    CONCURRENTLY = 329,
    CONFIGURATION = 330,
    CONNECTION = 331,
    CONSTRAINT = 332,
    CONSTRAINTS = 333,
    CONTENT_P = 334,
    CONTINUE_P = 335,
    CONVERSION_P = 336,
    COPY = 337,
    COST = 338,
    CREATE = 339,
    CROSS = 340,
    CSV = 341,
    CURRENT_P = 342,
    CURRENT_CATALOG = 343,
    CURRENT_DATE = 344,
    CURRENT_ROLE = 345,
    CURRENT_SCHEMA = 346,
    CURRENT_TIME = 347,
    CURRENT_TIMESTAMP = 348,
    CURRENT_USER = 349,
    CURSOR = 350,
    CYCLE = 351,
    DATA_P = 352,
    DATABASE = 353,
    DAY_P = 354,
    DEALLOCATE = 355,
    DEC = 356,
    DECIMAL_P = 357,
    DECLARE = 358,
    DEFAULT = 359,
    DEFAULTS = 360,
    DEFERRABLE = 361,
    DEFERRED = 362,
    DEFINER = 363,
    DELETE_P = 364,
    DELIMITER = 365,
    DELIMITERS = 366,
    DESC = 367,
    DICTIONARY = 368,
    DISABLE_P = 369,
    DISCARD = 370,
    DISTINCT = 371,
    DO = 372,
    DOCUMENT_P = 373,
    DOMAIN_P = 374,
    DOUBLE_P = 375,
    DROP = 376,
    EACH = 377,
    ELSE = 378,
    ENABLE_P = 379,
    ENCODING = 380,
    ENCRYPTED = 381,
    END_P = 382,
    ENUM_P = 383,
    ESCAPE = 384,
    EVENT = 385,
    EXCEPT = 386,
    EXCLUDE = 387,
    EXCLUDING = 388,
    EXCLUSIVE = 389,
    EXECUTE = 390,
    EXISTS = 391,
    EXPLAIN = 392,
    EXTENSION = 393,
    EXTERNAL = 394,
    EXTRACT = 395,
    FALSE_P = 396,
    FAMILY = 397,
    FETCH = 398,
    FILTER = 399,
    FIRST_P = 400,
    FLOAT_P = 401,
    FOLLOWING = 402,
    FOR = 403,
    FORCE = 404,
    FOREIGN = 405,
    FORWARD = 406,
    FREEZE = 407,
    FROM = 408,
    FULL = 409,
    FUNCTION = 410,
    FUNCTIONS = 411,
    GLOBAL = 412,
    GRANT = 413,
    GRANTED = 414,
    GREATEST = 415,
    GROUP_P = 416,
    HANDLER = 417,
    HAVING = 418,
    HEADER_P = 419,
    HOLD = 420,
    HOUR_P = 421,
    IDENTITY_P = 422,
    IF_P = 423,
    ILIKE = 424,
    IMMEDIATE = 425,
    IMMUTABLE = 426,
    IMPLICIT_P = 427,
    IN_P = 428,
    INCLUDING = 429,
    INCREMENT = 430,
    INDEX = 431,
    INDEXES = 432,
    INHERIT = 433,
    INHERITS = 434,
    INITIALLY = 435,
    INLINE_P = 436,
    INNER_P = 437,
    INOUT = 438,
    INPUT_P = 439,
    INSENSITIVE = 440,
    INSERT = 441,
    INSTEAD = 442,
    INT_P = 443,
    INTEGER = 444,
    INTERSECT = 445,
    INTERVAL = 446,
    INTO = 447,
    INVOKER = 448,
    IS = 449,
    ISNULL = 450,
    ISOLATION = 451,
    JOIN = 452,
    KEY = 453,
    LABEL = 454,
    LANGUAGE = 455,
    LARGE_P = 456,
    LAST_P = 457,
    LATERAL_P = 458,
    LC_COLLATE_P = 459,
    LC_CTYPE_P = 460,
    LEADING = 461,
    LEAKPROOF = 462,
    LEAST = 463,
    LEFT = 464,
    LEVEL = 465,
    LIKE = 466,
    LIMIT = 467,
    LISTEN = 468,
    LOAD = 469,
    LOCAL = 470,
    LOCALTIME = 471,
    LOCALTIMESTAMP = 472,
    LOCATION = 473,
    LOCK_P = 474,
    MAPPING = 475,
    MATCH = 476,
    MATERIALIZED = 477,
    MAXVALUE = 478,
    MEMORY_LIMIT = 479,
    MEMORY_SHARED_QUOTA = 480,
    MEMORY_SPILL_RATIO = 481,
    MINUTE_P = 482,
    MINVALUE = 483,
    MODE = 484,
    MONTH_P = 485,
    MOVE = 486,
    NAME_P = 487,
    NAMES = 488,
    NATIONAL = 489,
    NATURAL = 490,
    NCHAR = 491,
    NEXT = 492,
    NO = 493,
    NONE = 494,
    NOT = 495,
    NOTHING = 496,
    NOTIFY = 497,
    NOTNULL = 498,
    NOWAIT = 499,
    NULL_P = 500,
    NULLIF = 501,
    NULLS_P = 502,
    NUMERIC = 503,
    OBJECT_P = 504,
    OF = 505,
    OFF = 506,
    OFFSET = 507,
    OIDS = 508,
    ON = 509,
    ONLY = 510,
    OPERATOR = 511,
    OPTION = 512,
    OPTIONS = 513,
    OR = 514,
    ORDER = 515,
    ORDINALITY = 516,
    OUT_P = 517,
    OUTER_P = 518,
    OVER = 519,
    OVERLAPS = 520,
    OVERLAY = 521,
    OWNED = 522,
    OWNER = 523,
    PARSER = 524,
    PARTIAL = 525,
    PARTITION = 526,
    PASSING = 527,
    PASSWORD = 528,
    PLACING = 529,
    PLANS = 530,
    POSITION = 531,
    PRECEDING = 532,
    PRECISION = 533,
    PRESERVE = 534,
    PREPARE = 535,
    PREPARED = 536,
    PRIMARY = 537,
    PRIOR = 538,
    PRIVILEGES = 539,
    PROCEDURAL = 540,
    PROCEDURE = 541,
    PROGRAM = 542,
    QUOTE = 543,
    RANGE = 544,
    READ = 545,
    REAL = 546,
    REASSIGN = 547,
    RECHECK = 548,
    RECURSIVE = 549,
    REF = 550,
    REFERENCES = 551,
    REFRESH = 552,
    REINDEX = 553,
    RELATIVE_P = 554,
    RELEASE = 555,
    RENAME = 556,
    REPEATABLE = 557,
    REPLACE = 558,
    REPLICA = 559,
    RESET = 560,
    RESTART = 561,
    RESTRICT = 562,
    RETURNING = 563,
    RETURNS = 564,
    REVOKE = 565,
    RIGHT = 566,
    ROLE = 567,
    ROLLBACK = 568,
    ROW = 569,
    ROWS = 570,
    RULE = 571,
    SAVEPOINT = 572,
    SCHEMA = 573,
    SCROLL = 574,
    SEARCH = 575,
    SECOND_P = 576,
    SECURITY = 577,
    SELECT = 578,
    SEQUENCE = 579,
    SEQUENCES = 580,
    SERIALIZABLE = 581,
    SERVER = 582,
    SESSION = 583,
    SESSION_USER = 584,
    SET = 585,
    SETOF = 586,
    SHARE = 587,
    SHOW = 588,
    SIMILAR = 589,
    SIMPLE = 590,
    SMALLINT = 591,
    SNAPSHOT = 592,
    SOME = 593,
    STABLE = 594,
    STANDALONE_P = 595,
    START = 596,
    STATEMENT = 597,
    STATISTICS = 598,
    STDIN = 599,
    STDOUT = 600,
    STORAGE = 601,
    STRICT_P = 602,
    STRIP_P = 603,
    SUBSTRING = 604,
    SYMMETRIC = 605,
    SYSID = 606,
    SYSTEM_P = 607,
    TABLE = 608,
    TABLES = 609,
    TABLESPACE = 610,
    TEMP = 611,
    TEMPLATE = 612,
    TEMPORARY = 613,
    TEXT_P = 614,
    THEN = 615,
    TIME = 616,
    TIMESTAMP = 617,
    TO = 618,
    TRAILING = 619,
    TRANSACTION = 620,
    TREAT = 621,
    TRIGGER = 622,
    TRIM = 623,
    TRUE_P = 624,
    TRUNCATE = 625,
    TRUSTED = 626,
    TYPE_P = 627,
    TYPES_P = 628,
    UNBOUNDED = 629,
    UNCOMMITTED = 630,
    UNENCRYPTED = 631,
    UNION = 632,
    UNIQUE = 633,
    UNKNOWN = 634,
    UNLISTEN = 635,
    UNLOGGED = 636,
    UNTIL = 637,
    UPDATE = 638,
    USER = 639,
    USING = 640,
    VACUUM = 641,
    VALID = 642,
    VALIDATE = 643,
    VALIDATOR = 644,
    VALUE_P = 645,
    VALUES = 646,
    VARCHAR = 647,
    VARIADIC = 648,
    VARYING = 649,
    VERBOSE = 650,
    VERSION_P = 651,
    VIEW = 652,
    VIEWS = 653,
    VOLATILE = 654,
    WHEN = 655,
    WHERE = 656,
    WHITESPACE_P = 657,
    WINDOW = 658,
    WITH = 659,
    WITHIN = 660,
    WITHOUT = 661,
    WORK = 662,
    WRAPPER = 663,
    WRITE = 664,
    XML_P = 665,
    XMLATTRIBUTES = 666,
    XMLCONCAT = 667,
    XMLELEMENT = 668,
    XMLEXISTS = 669,
    XMLFOREST = 670,
    XMLPARSE = 671,
    XMLPI = 672,
    XMLROOT = 673,
    XMLSERIALIZE = 674,
    YEAR_P = 675,
    YES_P = 676,
    ZONE = 677,
    ACTIVE = 678,
    CONTAINS = 679,
    CPUSET = 680,
    CPU_RATE_LIMIT = 681,
    CREATEEXTTABLE = 682,
    CUBE = 683,
    DECODE = 684,
    DENY = 685,
    DISTRIBUTED = 686,
    DXL = 687,
    ERRORS = 688,
    EVERY = 689,
    EXCHANGE = 690,
    EXPAND = 691,
    FIELDS = 692,
    FILL = 693,
    FORMAT = 694,
    FULLSCAN = 695,
    GROUP_ID = 696,
    GROUPING = 697,
    HASH = 698,
    HOST = 699,
    IGNORE_P = 700,
    INCLUSIVE = 701,
    INITPLAN = 702,
    LIST = 703,
    LOG_P = 704,
    MASTER = 705,
    MEDIAN = 706,
    MISSING = 707,
    MODIFIES = 708,
    NEWLINE = 709,
    NOCREATEEXTTABLE = 710,
    NOOVERCOMMIT = 711,
    ORDERED = 712,
    OTHERS = 713,
    OVERCOMMIT = 714,
    PARTITIONS = 715,
    PERCENT = 716,
    PERSISTENTLY = 717,
    PROTOCOL = 718,
    QUEUE = 719,
    RANDOMLY = 720,
    READABLE = 721,
    READS = 722,
    REJECT_P = 723,
    REPLICATED = 724,
    RESOURCE = 725,
    ROLLUP = 726,
    ROOTPARTITION = 727,
    SCATTER = 728,
    SEGMENT = 729,
    SEGMENTS = 730,
    SETS = 731,
    SPLIT = 732,
    SQL = 733,
    SUBPARTITION = 734,
    THRESHOLD = 735,
    TIES = 736,
    VALIDATION = 737,
    WEB = 738,
    WRITABLE = 739,
    NULLS_FIRST = 740,
    NULLS_LAST = 741,
    WITH_ORDINALITY = 742,
    WITH_TIME = 743,
    POSTFIXOP = 744,
    UMINUS = 745
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

union YYSTYPE
{
#line 189 "gram.y" /* yacc.c:1909  */

	core_YYSTYPE		core_yystype;
	/* these fields must match core_YYSTYPE: */
	int					ival;
	char				*str;
	const char			*keyword;

	char				chr;
	bool				boolean;
	JoinType			jtype;
	DropBehavior		dbehavior;
	OnCommitAction		oncommit;
	List				*list;
	Node				*node;
	Value				*value;
	ObjectType			objtype;
	TypeName			*typnam;
	FunctionParameter   *fun_param;
	FunctionParameterMode fun_param_mode;
	FuncWithArgs		*funwithargs;
	DefElem				*defelt;
	SortBy				*sortby;
	WindowDef			*windef;
	JoinExpr			*jexpr;
	IndexElem			*ielem;
	Alias				*alias;
	RangeVar			*range;
	IntoClause			*into;
	WithClause			*with;
	A_Indices			*aind;
	ResTarget			*target;
	struct PrivTarget	*privtarget;
	AccessPriv			*accesspriv;
	InsertStmt			*istmt;
	VariableSetStmt		*vsetstmt;

#line 582 "gram.h" /* yacc.c:1909  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif

/* Location type.  */
#if ! defined YYLTYPE && ! defined YYLTYPE_IS_DECLARED
typedef struct YYLTYPE YYLTYPE;
struct YYLTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
};
# define YYLTYPE_IS_DECLARED 1
# define YYLTYPE_IS_TRIVIAL 1
#endif



int base_yyparse (core_yyscan_t yyscanner);

#endif /* !YY_BASE_YY_GRAM_H_INCLUDED  */