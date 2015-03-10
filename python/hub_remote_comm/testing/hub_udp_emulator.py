#!/usr/bin/python
# 
import SocketServer
from socket import *

class MyUDPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # get the data packet.
        #  parse it to get the umid
        data = self.request[0].strip()
        dl = data.split()
        umid = dl[-1]
        #  configure the acknowledgement
        respmsg = "RCVD %s",umid
        #  send it back to the specified acknowledgement port
        send_resp = False
        if send_resp:
            ipaddr = self.client_address[0]
            port = 44823
            cl_socket = socket(AF_INET,SOCK_DGRAM)
            srv_addr = (ipaddr,port)
            cl_socket.sendto(respmsg,srv_addr)

        #print "{} wrote:".format(self.client_address[0])
        print "debug client address: ",self.client_address
        print data
        #socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    print "serving forever on localhost port 44800"
    HOST, PORT = "localhost", 44800
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()

