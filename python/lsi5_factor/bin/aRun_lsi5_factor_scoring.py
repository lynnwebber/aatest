#!/usr/bin/python
# -----------------------------------------------------------------
#    * NOTICE *           * NOTICE *             * NOTICE *
# -----------------------------------------------------------------
#  Copyright 2008 and beyond, neoPsy Systems
#  Copyright 2008 and beyond, Somerville Partners LLC.
#                       ALL RIGHTS RESERVED
#  ENFORCABLE UNDER COPYRIGHT LAW OF THE UNITED STATES OF AMERICA. 
#  Use, duplication, or disclosure of this software in part or in 
#  full is prohibited without the written concent of neoPsy Systems
#  or Somerville Partners LLC.
# -----------------------------------------------------------------
# 
import dimscores as ds
import calc
import cache
import config as cfg
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
if cfg.service.environment == "unix":
    from SocketServer import ForkingMixIn
elif cfg.service.environment == "windows":
    from SocketServer import ThreadingMixIn

# put a class here for processing
class snpLSI5FacScoring:
    def scoreFactors(self,rsxml):
        """
        scoreFactors - calculates the lsi factor scores
        Arguments: rawscore_xml(string)
        Returns: lsi_dim_score_xml(string) or error-xml(string)
        """
        rv = ''
        if not ds.xml.parse(rsxml):
            rv = "<error>Rawscore parsing error</error>"
        else:
            calc.calc_factors()
            calc.calc_styles()
            rv = cache.gen_outstream()
            cache.debug.purge()
            cache.score.purge()
        return rv

    def ServiceVerify(self):
        rv = "<verification>"
        rv += "  <service>LSI Factor Scoring</service>"
        rv += "  <version>0.1</version>"
        rv += "  <status>Available</status>"
        rv += "</verification>"
        return rv

# -----------------------------------------------------------------
# 
# use forking server for unix/linux or the threading server for 
# windows as specified in the config file
#
serveraddr = (cfg.service.host,cfg.service.port)
if cfg.service.environment == "unix":
    class ForkingServer(ForkingMixIn, SimpleXMLRPCServer): pass
    srvr = ForkingServer(serveraddr, SimpleXMLRPCRequestHandler)
elif cfg.service.environment == "windows":
    class ThreadingServer(ThreadingMixIn, SimpleXMLRPCServer): pass
    srvr = ThreadingServer(serveraddr, SimpleXMLRPCRequestHandler)

srvr.register_instance(snpLSI5FacScoring())
srvr.register_introspection_functions()

try:
    print '-'*60
    print 'LSI 5-Factor Scoring xml-rpc service started'
    print '  Startup host and port:',serveraddr
    print '-'*60
    print '   Use Control-C to exit'
    print '-'*60
    srvr.serve_forever()
except KeyboardInterrupt:
    print 'Exiting - Service Stopped'

