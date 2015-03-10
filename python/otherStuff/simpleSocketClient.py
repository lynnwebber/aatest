#!/usr/bin/python
#
import socket
from optparse import OptionParser

## command line stuff
#
def setup_cl_options(p):
    p.add_option('-p','--port',dest="port",
                    help="port number for socket connection (required)")
    p.add_option("--append",action="store_true",dest="append",
                    help="open the output file in append mode")

def validate_cl_options(o,p):
    if not o.port:
        msg = "port not specified"
        p.error(msg)

def get_cl():
    usage = "usage: %prog [options] host"
    clparser = OptionParser(usage)
    setup_cl_options(clparser)
    (clopts,args) = clparser.parse_args()
    validate_cl_options(clopts,clparser)
    return (clopts,args)

#
## end command line stuff

## socket stuff
#
def test_socket(host,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,44823))
    s.sendall("hello over there\r\n")

    while 1:
        buff = s.recv(1024)
        if not len(buff):
            break
        print buff

#
## end socket stuff




def main():
    (clopts,args) = get_cl()

    print "testing host: %s  on port: %s" % (args[0],clopts.port)
    test_socket(args[0],clopts.port)

# -------------------------------------------------------------
if __name__ == "__main__":
    main()


