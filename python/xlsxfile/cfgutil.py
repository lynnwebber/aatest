#!/usr/bin/env python
#
import sys
import argparse
import csv
import xlTags as xt
import xlSite as xs
import kepware as kep
import v3xml as v3x

# -------------------------------------------------------------
#   command line parsing
# -------------------------------------------------------------
def process_commandline():

    # setup the parser object
    desc = "V3 Configuration Generation Utility"
    usage = "usage: %prog [options]"
    p = argparse.ArgumentParser(description=desc)

    # setup options
    p.add_argument('-a','--action',dest="action",
            action="store",
            choices=['genkepload','genxml'],
            required=True,
            help="desired action for the script to process")

    p.add_argument('-s','--spreadsheet',
            dest="spreadsheet",
            action="store",
            help="input spreadsheet file")

    p.add_argument('-o','--output',
            dest="outfile",
            action="store",
            help="output file for the action chosen")

    p.add_argument('-x','--xml',
            dest="xmlfile",
            action="store",
            help="XML file to be processed")

    p.add_argument('-v','--verbose',
            dest="verbose",
            action="store_true",
            default=False,
            help="script will display detailed run messages")
    # parse
    rv = p.parse_args()
    # validate
    if rv.action == "genkepload":
        if rv.spreadsheet == None:
            p.error("No input spreadsheet specified - required for this action")
        if rv.outfile == None:
            p.error("No output file name specified - required for this action")
    if rv.action == "genxml":
        if rv.spreadsheet == None:
            p.error("No input spreadsheet specified - required for this action")
        if rv.xmlfile == None:
            p.error("No XML file name specified - required for this action")

    return rv

# -------------------------------------------------------------
def main():
    args = process_commandline()

    if args.action == "genkepload":
        try:
            recs = xt.load_and_correct_tags(args)
            kep.generate_kepware_load(args,recs)
        except ValueError as e:
            print(e)
            sys.exit(-1)

    if args.action == "genxml":
        try:
            siterecs = xs.load_site_info(args)
            tagrecs = xt.load_and_correct_tags(args)
            v3x.build_xml(args,siterecs,tagrecs)
        except ValueError as e:
            print(e)
            sys.exit(-1)


# -------------------------------------------------------------
if __name__ == "__main__":
    main()
