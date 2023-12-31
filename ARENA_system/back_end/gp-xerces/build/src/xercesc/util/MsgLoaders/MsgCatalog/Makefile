
srcdir = ../../../../../../src/xercesc/util/MsgLoaders/MsgCatalog
top_srcdir = ../../../../../..
top_builddir = ../../../../..
prefix = /usr/local
INSTALL = /usr/bin/install -c
INSTALL_PROGRAM = ${INSTALL}
mkdir_p = $(MKDIR_P)

include $(top_srcdir)/version.incl

# No conventional target - this dir is resources only.
TARGET=
CLEANFILES += $(RESFILES)

# Resource shortname
PKGNAME=XercesMessages

# target file for resource bundle - this must be set, or 'make all' won't
# build any resources.
RESTARGET=$(top_builddir)/src/.libs/$(PKGNAME)_en_US.cat

# Resource files.  Add new ones for additional locales here.
# keep in sync with the file RESLIST
RESFILES=$(PKGNAME)_en_US.cat

# list of targets that aren't actually created
.PHONY: report 

check: all

all: $(RESTARGET) $(TARGET)  

$(RESTARGET): $(RESFILES)
	@echo building $(RESTARGET)
	$(mkdir_p) $(top_builddir)/src/.libs
	cp $(RESFILES) $(top_builddir)/src/.libs
	
# clean out files
distclean clean: $(CLEAN_SUBDIR)
	-rm -f $(RESTARGET)

## resources
$(PKGNAME)_%.cat: $(srcdir)/$(PKGNAME)_%.Msg
	@echo "generating $@"
	gencat $@ $^

# for installing the library
# for installing the library
install: $(RESTARGET)
	$(mkdir_p) $(prefix)/msg
	$(INSTALL_PROGRAM) $(RESTARGET) $(prefix)/msg

uninstall: 
	-rm -f $(prefix)/msg/$(RESFILES)


# Needed to support "make dist"
distdir:
	@srcdirstrip=`echo "$(srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	topsrcdirstrip=`echo "$(top_srcdir)" | sed 's/[].[^$$\\*]/\\\\&/g'`; \
	list='XercesMessages_en_US.Msg Makefile.in'; \
	  dist_files=`for file in $$list; do echo $$file; done | \
	  sed -e "s|^$$srcdirstrip/||;t" \
	      -e "s|^$$topsrcdirstrip/|$(top_builddir)/|;t"`; \
	case $$dist_files in \
	  */*) $(MKDIR_P) `echo "$$dist_files" | \
			   sed '/\//!d;s|^|$(distdir)/|;s,/[^/]*$$,,' | \
			   sort -u` ;; \
	esac; \
	for file in $$dist_files; do \
	  if test -f $$file || test -d $$file; then d=.; else d=$(srcdir); fi; \
	  if test -d $$d/$$file; then \
	    dir=`echo "/$$file" | sed -e 's,/[^/]*$$,,'`; \
	    if test -d $(srcdir)/$$file && test $$d != $(srcdir); then \
	      cp -pR $(srcdir)/$$file $(distdir)$$dir || exit 1; \
	    fi; \
	    cp -pR $$d/$$file $(distdir)$$dir || exit 1; \
	  else \
	    test -f $(distdir)/$$file \
	    || cp -p $$d/$$file $(distdir)/$$file \
	    || exit 1; \
	  fi; \
	done
