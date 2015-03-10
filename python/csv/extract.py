#!/usr/bin/python
#
from optparse import OptionParser
import csv

# -------------------------------------------------------------
#   command line parsing 
# -------------------------------------------------------------
def setup_cl_options(p):
    p.add_option('-c','--csv',dest="csvfile",
                    help="comma seperated values input file")
    p.add_option('-o','--output',dest="outfile",
                    help="output file name")

def validate_cl_options(o,p):
    if not o.csvfile:
        msg = 'no csv file specified.  REQUIRED'
        p.error(msg)

# -------------------------------------------------------------
#  csv stuff 
# -------------------------------------------------------------
def read_csv(fn):
    pull_list = ['Diamond T 43-5','Palm 32-19']
    fld_list = 'RTU_name RTU_id RTU_num DiffP LineP LineT Water FlowMCF FlowTime WaterLevel CasingP DownholeP MMBTU'.split()
    rdr = csv.reader(open(fn,'rb'))
    for row in rdr:
        #print '|'.join(row)
        cleanrow = [x.strip() for x in row]
        if cleanrow != []:
            if cleanrow[0] in pull_list:
                print zip(fld_list,cleanrow)

# -------------------------------------------------------------
def main():
    usage = "usage: %prog [options] arg"
    clparser = OptionParser(usage)
    setup_cl_options(clparser)
    (clopts,args) = clparser.parse_args()
    validate_cl_options(clopts,clparser)

    print "the csvfile is: %(csvfile)s" % {'csvfile':clopts.csvfile}
    read_csv(clopts.csvfile)

# -------------------------------------------------------------
if __name__ == "__main__":
    main()


