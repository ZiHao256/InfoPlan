#!/usr/bin/env python
import os
import re
import sys
import tempfile

from gppylib.gpparseopts import OptParser, OptChecker
from gppylib.commands.base import Command, LOCAL

description = ("""
This utility is NOT SUPPORTED and is for internal-use only.

updates the pg_hba.conf file for segments.
""")

def parseargs():
    parser = OptParser(option_class=OptChecker, description=' '.join(description.split()))

    parser.setHelp([])

    parser.add_option('-d', '--data-dir', dest='datadir', metavar='<data dir of the segment>',
                      help='Data dir of the segment to update pg_hba.conf')
    parser.add_option("-e", "--entries", dest="entries", metavar="<entries to be added>",
                      help="entries to be added to pg_hba.conf")
    options, args = parser.parse_args()
    return validate_args(options)

def validate_args(options):
    if not options.datadir:
        sys.stderr.write("--file required")
        sys.exit(1)

    if not options.entries:
        sys.stderr.write("--entries required")
        sys.exit(1)

    return options

def lineToCanonical(s):
    s = s.strip()
    s = re.sub("\s+", " ", s) # reduce whitespace runs to single space
    return s

def read_from_hba_file_and_get_empty_tempfile(hba_filename):
    with open(hba_filename, 'r') as infile:
        lines = infile.readlines()

    (tempFD, temp_hba_filename) = tempfile.mkstemp(prefix="pg_hba", suffix=".tmp", dir=os.path.abspath(os.path.dirname(hba_filename)))

    os.chmod(os.path.abspath(temp_hba_filename), os.stat(os.path.abspath(hba_filename)).st_mode)
    return lines, temp_hba_filename

def write_entries(out_entries, temp_hba_filename, hba_filename):
    with open(temp_hba_filename, 'w') as outfile:
        outfile.write('\n'.join(out_entries))
        outfile.write('\n')
    os.rename(os.path.abspath(temp_hba_filename), hba_filename)

def remove_dup_add_entries(lines, entries):
    existingLineMap = {}
    out_entries = []
    for line in lines:
        canonical = lineToCanonical(line)
        if canonical not in existingLineMap:
            existingLineMap[canonical] = True
            out_entries.append(line.strip())

    for entry in entries.split('\n'):
        if entry not in existingLineMap:
            existingLineMap[entry] = True
            out_entries.append(entry)

    return out_entries

def run_pg_ctl_reload(datadir):
    name = "pg_ctl reload"
    cmd_str = "$GPHOME/bin/pg_ctl reload -D %s" % datadir
    cmd = Command(name, cmd_str, ctxt=LOCAL)
    cmd.run(validateAfter=True)

def main():
    options = parseargs()
    hba_filename = options.datadir +'/pg_hba.conf'
    lines, temp_hba_filename = read_from_hba_file_and_get_empty_tempfile(hba_filename)
    out_entries = remove_dup_add_entries(lines, options.entries)
    write_entries(out_entries, temp_hba_filename, hba_filename)
    run_pg_ctl_reload(options.datadir)

if __name__ == "__main__":
    main()
