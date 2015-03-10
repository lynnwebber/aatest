#!/usr/bin/python
#
from optparse import OptionParser

# -------------------------------------------------------------
#   command line parsing 
# -------------------------------------------------------------
def process_commandline():
    # setup the parser object
    desc = "Build pod (optionally) and sensors for POD to load from CIRIS CSV file"
    usage = "usage: %prog [options]"
    p = OptionParser(usage=usage,description=desc)
    # setup options
    p.add_option('-d','--desc',
                dest="description",
                help="pod description string (in quotes if spaces) "
                    "cannot be used with -n option")
    p.add_option('-n','--nopodcreation',
                dest="nopod", action="store_true", default=False,
                help="do not create a pod (must be used with -p option)")
    p.add_option('-p','--podid',
                dest="podid",
                help="pod (podid) where the sensors will be added "
                    "Note: must be used with -n option")
    # parse
    (opts,args) = p.parse_args()
    rv = [opts,args]
    # check errors
    if opts.nopod:
        if opts.description:
            msg = "cannot specifiy a description if you are not creating a pod"
            p.error(msg)
            rv = []
        if not opts.podid:
            msg = "you did not specify a pod for sensor creation"
            p.error(msg)
            rv = []
    if not opts.nopod:
        if not opts.description:
            msg = 'a description is required to build a POD'
            p.error(msg)
            rv = []
        if opts.podid:
            msg = "you cannot specify a podid without using the -n option"
            p.error(msg)
            rv = []
        if len(args) > 0:
            msg = 'it appears that you have entered a description without quotes'
            p.error(msg)
            rv = []
    # return
    return rv

# -------------------------------------------------------------
def main():
    (opts,args) = process_commandline()
    
    print "opts:",opts
    print "args:",args
# -------------------------------------------------------------
if __name__ == "__main__":
    main()


