#!/usr/bin/env python
#
import sys
import argparse
import csv
import excel_functions as xf
import config as cfg

# -------------------------------------------------------------
#   command line parsing
# -------------------------------------------------------------
def process_commandline():

    # setup the parser object
    desc = "V3 Configuration Generation Utility"
    usage = "usage: %prog [options]"
    p = argparse.ArgumentParser(description=desc)

    # setup options
    p.add_argument('--action',dest="action", 
            action="store",
            choices=['GenKepLoad'],
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
    
    #p.add_argument('-x','--xml',
    #        dest="xmlfile",
    #        action="store",
    #        help="XML file to be processed")
    
    p.add_argument('-v','--verbose',
            dest="verbose", 
            action="store_true", 
            default=False,
            help="script will display detailed run messages")
    # parse
    rv = p.parse_args()
    # validate
    if rv.action == "GenKepLoad":
        if rv.spreadsheet == None:
            p.error("No input spreadsheet specified - required for this action")
        if rv.outfile == None:
            p.error("No output file name specified - required for this action")
    
    return rv
 
# -------------------------------------------------------------
def generate_kepware_load(args):
    """
    generate a kepware load CSV file using the data that was provided in 
    the spreadsheet
    """
    err, recs = xf.load_and_correct_spreadsheet(args)
    if err:
        sys.exit(0)

    with open(args.outfile,'w') as csvout:
        writer = csv.DictWriter(csvout,fieldnames=cfg.kepware_load_header)
        writer.writeheader()
        for rec in recs:
            print('debugging: ',rec)
            csvdict = {'Tag Name' : rec['Tag_Name'],
                    'Address' : rec['SCADA_Address'],
                    'Data Type' : rec['SCADA_Data_Type'],
                    'Respect Data Type' : '1',
                    'Client Access' : rec['Client_Access'],
                    'Scan Rate' : '100',
                    'Scaling' : '',
                    'Raw Low' : '',
                    'Raw High' : '',
                    'Scaled Low' : '',
                    'Scaled High' : '',
                    'Scaled Data Type' : '',
                    'Clamp Low' : '',
                    'Clamp High' : '',
                    'Eng Units' : '',
                    'Description' : rec['Tag_Description'],
                    'Negate Value' : ''}
            writer.writerow(csvdict)
            print("Tag: %s" % (rec['Tag_Name']))

# -------------------------------------------------------------
def main():
    args = process_commandline()
   
    err = False
    if args.action == "GenKepLoad":
        err = generate_kepware_load(args)

    if err:
        print("An error was detected in the run - please review messages")
    

# -------------------------------------------------------------
if __name__ == "__main__":
    main()
