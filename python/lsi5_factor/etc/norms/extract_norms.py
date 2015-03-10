#!/usr/bin/env python
# -----------------------------------------------------------------
#    * NOTICE *           * NOTICE *             * NOTICE *
# -----------------------------------------------------------------
#  Copyright 2008 and beyond, neoPsy Systems
#  Copyright 2008 and beyond, Somerville Partners LLC.
#                       ALL RIGHTS RESERVED
#  ENFORCABLE UNDER COPYRIGHT LAW OF THE UNITED STATES OF AMERICA. 
#  Use, duplication, or disclosure of this software in part or in 
#  full is prohibited without the written concent of neoPsy Systems
#  or Somerville Partners LLC.
# -----------------------------------------------------------------
# 

import os, sys
import xlrd as xl
from elementtree.SimpleXMLWriter import XMLWriter
import decimal as dec
from exceptions import *
from types import *
from optparse import OptionParser

# ----------------------------------------------------------------
# check/get/set command line options
#
def getCommandLine():
    usage =  "%prog [options] SOURCEFILE"
    ver = "0.1a"
    desc = "Program extracts scoring norms and variance information from "
    desc += "an excel spreadsheet (SOURCEFILE) specifically designed to hold "
    desc += "the factor norm information."
    desc += "\nNote:  The file should include both 5 and 6 factor norms."
    parser = OptionParser(usage=usage,version=ver,description=desc)
    parser.add_option("-v","--verbose",dest="verbose",default=False,
                    action="store_true",
                    help="print status messages as processing occurs")
    (opts, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("argument error - must provide filespec")
    
    return args[0],opts


# ----------------------------------------------------------------
def cvt2Dec(theNum, precision=10):
    """ 
    Convert a number to a Decimal format.
    
    Optionally, include a precision 
      (will default to 10 places right of decimal point)
    """
    #
    # Decimal class objects can only be converted from strings.
    #  So get 'theNum' into string type
    #
    num_str = theNum
    if isinstance(theNum,(int, long, float)):     # if the number is already numeric
        num_str = repr(theNum)                    #  convert it to a string
    #
    # Decimal class precision seems to include all digits on both sides of the 
    # decimal point.  NOT what I want!!
    # Increase requested precision by the number of digits
    # to the left of decimal point
    #
    prec = precision
    tmp = float(num_str)
    if (tmp > 1):
        tmp = len(str(int(tmp)))
        prec += tmp
    del tmp                           # I'm done with tmp
    #
    # Convert the number to Decimal class.  
    # Return Decimal value, normalized to requested precision
    #
    val = dec.Decimal(num_str)
    dec.getcontext().prec=prec
        
    return str(val.normalize())

# ----------------------------------------------------------------
# validate the workbook
#
def validate_workbook(wbfile):

    req_sheets = ["5FactorNorms","6FactorNorms"]

    try:                            
        theBook = xl.open_workbook(wbfile)
    except xl.XLRDError:
        print "*** Open failed: %s: %s" % sys.exc_info()[:2]
        sys.exit(2)
    except:
        print "*** Open failed: %s: %s" % sys.exc_info()[:2]
        sys.exit(2)  
    
    #
    # Get list of worksheet names, and validate minimum required
    #   worksheets are present.
    #
    sheets=theBook.sheet_names()
    for sh in req_sheets:
        if sh not in sheets:
            print "*** Invalid Workbook -- missing sheet: %s" % (sh)
            sys.exit(2)

    return theBook
    

# ----------------------------------------------------------------
# extract success profile information
#
def extract_factor_norms(theBook,normsType):
    """
    Extract the factor norm information
    Call with: workbook object
    Return: list of lists
    """
    rv = []

    if normsType == 5:
        theSheet = theBook.sheet_by_name("5FactorNorms")
    elif normsType == 6:
        theSheet = theBook.sheet_by_name("6FactorNorms")

    right_label = theSheet.col(0)   # Col A
    mean = theSheet.col(1)          # col B
    stddev = theSheet.col(2)        # col C
    left_label = theSheet.col(3)    # col D
    calctype = theSheet.col(4)      # col e
    dims = theSheet.col(5)          # col f

    #
    # now loop through the sheet extracting info from each column
    #
    for x in range(theSheet.nrows-1):
        fac = str(right_label[x+1].value).strip().replace(' ','-').lower()
        mn = cvt2Dec(mean[x+1].value)
        sd = cvt2Dec(stddev[x+1].value)
        facop = str(left_label[x+1].value).strip().replace(' ','-').lower()
        ct = str(calctype[x+1].value).strip().lower()
        dl = str(dims[x+1].value).strip().replace(' ','-').lower()
        rv.append([fac,mn,sd,facop,ct,dl])

    return rv

# ----------------------------------------------------------------
# build an output file
#
def list_to_file(thelist,thefile):
    """
    Take a list of lists and output it to the given filename
    delimited by pipe symbols
    Returns: nothing
    """
    fobj = open(thefile,'w')
    for x in thelist:
        y = '|'.join(x)
        fobj.write(y+'\n')
    fobj.close()
    
# ----------------------------------------------------------------
# main program module
#
def main():

    # get all the stuff from the command line
    #
    infile,opts = getCommandLine()
    if opts.verbose: print "Starting extraction"

    if opts.verbose: print "\tvalidating workbook sheets"
    theBook = validate_workbook(infile)

    if opts.verbose: print "\textracting data"

    data5 = extract_factor_norms(theBook,5)
    data6 = extract_factor_norms(theBook,6)

    if opts.verbose: print "\twriting data to output"
    list_to_file(data5,"lsi_5factor.txt")
    list_to_file(data6,"lsi_6factor.txt")

    if opts.verbose: print "Completed"


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    main()
