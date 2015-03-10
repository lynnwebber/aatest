#!/usr/bin/python
# 
import SocketServer
from socket import *
import config as cfg
import logging

#
# setup logging
logger = logging.getLogger("HUBCommLogger")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(cfg.service.logfile)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

class UDPLoggerHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        ipfrom = self.client_address[0]
        msg = "from: %s received: %s" % (ipfrom,data)
        logger.info(msg)
        print 'debug:  rawdata -> ',data
        print 'debug: log msg -> ',msg

# -----------------------------------------------------------------
# setup the server
serveraddr = (cfg.service.host,cfg.service.port)
server = SocketServer.UDPServer(serveraddr, UDPLoggerHandler)

#
# now its time to start things up

try:
    logger.info('------ Starting service --------')
    print '-'*60
    print 'HUB Remote Communication logger UDP service started'
    print '  Startup host and port:',serveraddr
    print '-'*60
    print '   Use Control-C to exit'
    print '-'*60
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting - Service Stopped'

