#!/usr/bin/python

# udp_client.py
#
# UDP client to send command to HUB
#

import os, sys
from socket import *

# get and parse args
def parse_args():
    tmp = []
    for x in sys.argv[1].split('|'):
        tmp.append(x.split(':'))
    rv = dict(tmp)
    return rv
        
    
# configure outgoing message
def build_msg(argd):
    msg = 'MODBUS %(slv)s %(fnc)s %(addr)s %(val)s %(umid)s' % argd
    return msg

# setup and call server
def send_hub_msg(ipaddr, port=44800, msg=''):
    cl_socket = socket(AF_INET,SOCK_DGRAM)
    srv_addr = (ipaddr,port)
    cl_socket.sendto(msg,srv_addr)

# handle response

# main
def main():
    childpid = os.getpid()
    argd = parse_args()
    argd['umid'] = childpid
    msgstr = build_msg(argd)
    ipaddr = argd['ip']
    send_hub_msg(ipaddr,msg=msgstr)

# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    main()
