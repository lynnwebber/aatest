#!/usr/bin/python
#
from optparse import OptionParser
import csv

# -------------------------------------------------------------
#   command line parsing 
# -------------------------------------------------------------
def setup_cl_options(p):
    p.add_option('-o','--operator_file',dest="opfile",
                    help="comma seperated values input operator file with muids file")
    p.add_option('-p','--phone_list',dest="phonelist",
                    help="comma seperated values input phone number list")

def validate_cl_options(o,p):
    if not o.opfile:
        msg = 'no operator file specified.  REQUIRED'
        p.error(msg)
    if not o.phonelist:
        msg = 'no phonelist file specified.  REQUIRED'
        p.error(msg)

# -------------------------------------------------------------
#  csv stuff 
# -------------------------------------------------------------
def read_operator_file(fn):
    rv = []
    fld_list = 'podid operatorid description config_id active muid provider'.split()
    rdr = csv.reader(open(fn,'rb'))
    for row in rdr:
        #print '|'.join(row)
        cleanrow = [x.strip() for x in row]
        if cleanrow != []:
                tmp = zip(fld_list,cleanrow)
                rv.append(dict(tmp))
    return rv

# -------------------------------------------------------------
def read_phone_num_list(fn):
    rv = []
    fld_list = 'WirelessNumber UserName ServiceStatus UpgradeDate AccountNumber DeviceID'.split()
    rdr = csv.reader(open(fn,'rb'))
    for row in rdr:
        #print '|'.join(row)
        cleanrow = [x.strip() for x in row]
        if cleanrow != []:
                #print zip(fld_list,cleanrow)
                rv.append(cleanrow[0].replace('-',''))
    return rv

# -------------------------------------------------------------
def compare(plist,oplist):
    for d in oplist:
        pod = d['podid']
        op = d['operatorid']
        desc = d['description']
        config = d['config_id']
        active = d['active']
        muid = d['muid']
        provider = d['provider']

        if muid in plist:
            print '%s,%s,%s,%s,%s,%s,Verizon' % (pod,op,desc,config,active,muid)
        else:
            print '%s,%s,%s,%s,%s,%s,ATT' % (pod,op,desc,config,active,muid)




# -------------------------------------------------------------
def main():
    usage = "usage: %prog [options] arg"
    clparser = OptionParser(usage)
    setup_cl_options(clparser)
    (clopts,args) = clparser.parse_args()
    validate_cl_options(clopts,clparser)

    plist = read_phone_num_list(clopts.phonelist)
    oplist = read_operator_file(clopts.opfile)
    compare(plist,oplist)
    

# -------------------------------------------------------------
if __name__ == "__main__":
    main()


