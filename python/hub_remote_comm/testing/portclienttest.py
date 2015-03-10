#!/usr/bin/python
# 
import SocketServer
from socket import *

send_resp = True
if send_resp:
    ipaddr = '155.229.187.12'
    port = 44821
    respmsg = "this is a test"
    cl_socket = socket(AF_INET,SOCK_DGRAM)
    srv_addr = (ipaddr,port)
    cl_socket.sendto(respmsg,srv_addr)
