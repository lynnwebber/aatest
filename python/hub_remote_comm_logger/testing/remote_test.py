#!/usr/bin/python

# udp_client.py
#
# UDP client to send test msg
#

import os, sys
from socket import *
import time

# setup and call server
def send_udp_msg(ipaddr='155.229.187.12', port=44823, msg=''):
    cl_socket = socket(AF_INET,SOCK_DGRAM)
    srv_addr = (ipaddr,port)
    cl_socket.sendto(msg,srv_addr)

# handle response

# main
def main():
    argd = {}
    argd['umid'] = 1234
    msgstr = 'RCVD %(umid)s' % argd
    send_udp_msg(msg=msgstr)
    time.sleep(1)
    msgstr = 'MODBUS %(umid)s SUCCESS' % argd
    send_udp_msg(msg=msgstr)

# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    main()
