#!/usr/bin/python
#
import sys
import argparse
import query_functions as qry

# -------------------------------------------------------------
#   command line parsing
# -------------------------------------------------------------
def process_commandline():

    # setup the parser object
    desc = "Move a site from one operator to another (including equipment, tags, and groups)"
    usage = "usage: %prog [options]"
    p = argparse.ArgumentParser(description=desc)

    # setup options
    p.add_argument('-r','--rtuid',dest="newrtuid",action="store",required=True,
                help="newly assigned rtuid (number)")
    p.add_argument('-v','--verbose',dest="verbose", action="store_true", default=False,
                help="script will display detailed messages")
    p.add_argument('-d','--debug',dest="debug", action="store_true", default=False,
                help="script will run in debug mode")
    # parse
    rv = p.parse_args()
    return rv


# -------------------------------------------------------------
def find_data(dbconn,args):
    # get the config IDs for the given rtuid 
    cfg_list = []
    cfgs = qry.find_configs_for_rtuid(args.newrtuid,dbconn)
    for cfg in cfgs:
        cfgid = cfg[0]
        major = cfg[2]
        minor = cfg[3]
        cfg_list.append([cfgid,major,minor])

    pod_list = []
    pods = qry.find_pods_for_rtuid(args.newrtuid,dbconn)
    for pod in pods:
        seq = pod[0]
        podid = pod[2]
        major = pod[3]
        minor = pod[4]
        pod_list.append([podid,major,minor,seq])
    

    return cfg_list,pod_list


# -------------------------------------------------------------
def main():
    args = process_commandline()

    if args.verbose: print "Opening Database connection"
    dbconn = qry.connection()

    config_list,pod_list = find_data(dbconn,args)
    print 'debug: configs',config_list
    print 'debug: pods',pod_list

    if args.verbose: print "Closing Database connection"
    dbconn.close()
# -------------------------------------------------------------
if __name__ == "__main__":
    main()
