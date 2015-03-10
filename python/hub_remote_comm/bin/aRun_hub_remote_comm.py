#!/usr/bin/python
# 
import inputParser as ireq
import dataProcessing as dp
import subManager as sm
import config as cfg
import logging

from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
if cfg.service.environment == "unix":
    from SocketServer import ForkingMixIn
elif cfg.service.environment == "windows":
    from SocketServer import ThreadingMixIn

#
# setup logging
logger = logging.getLogger("HUBCommSvc")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(cfg.service.logfile)
formatter = logging.Formatter('%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# put a class here for processing
class wkHubCommSvc:
    def sendHubMsg(self,inxml):
        """
        sends a message to the hub specified in the request
        """
        rv = ''
        if not ireq.reqdata.parse(inxml):
            rv = "<error>Request XML parsing error</error>"
            logger.error('xml parsing error:'+inxml)
        else:
            # setup the call parameters to the child process
            params = dp.gen_outstream()
            # kick off the child process
            sm.run_sub(params)
            # return success message
            rv = '<success>The message has been queued for delivery</success>'
            logger.info('successfully processed -> '+params)
        return rv

    def ServiceVerify(self):
        rv = "<verification>"
        rv += "  <service>HUB Message Communication</service>"
        rv += "  <status>Available</status>"
        rv += "</verification>"
        return rv

# -----------------------------------------------------------------
# 
# use forking server for unix/linux or the threading server for 
# windows as specified in the config file
#
# setup the server
serveraddr = (cfg.service.host,cfg.service.port)
if cfg.service.environment == "unix":
    class ForkingServer(ForkingMixIn, SimpleXMLRPCServer): pass
    srvr = ForkingServer(serveraddr, SimpleXMLRPCRequestHandler)
elif cfg.service.environment == "windows":
    class ThreadingServer(ThreadingMixIn, SimpleXMLRPCServer): pass
    srvr = ThreadingServer(serveraddr, SimpleXMLRPCRequestHandler)

srvr.register_instance(wkHubCommSvc())
srvr.register_introspection_functions()

#
# now its time to start things up

try:
    logger.info('------ Starting service --------')
    print '-'*60
    print 'HUB Remote Communication xml-rpc service started'
    print '  Startup host and port:',serveraddr
    print '-'*60
    print '   Use Control-C to exit'
    print '-'*60
    srvr.serve_forever()
except KeyboardInterrupt:
    print 'Exiting - Service Stopped'

