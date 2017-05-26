#!/usr/bin/python
#

import os
import logging
import xmlrpclib
import config as cfg

# ----------------------------------------------------------------
def check_processes(logger,procinfo):
    for proc in procinfo:
        print proc['name'],' - ',proc['statename']

# ----------------------------------------------------------------
def manager(logger):
    for srvr in cfg.server_list:
        print "trying server",srvr
        srv =  xmlrpclib.Server(srvr)
        try:
            state = srv.supervisor.getState()['statename']
            msg = "conencted to server: %s - status: %s" % (srvr,state)
            logger.info(msg)
            procinfo = srv.supervisor.getAllProcessInfo()
            check_processes(logger,procinfo)
        except: 
            print "processing error - check log"
            msg = "error processing server: %s " % (srvr)
            logger.error(msg)

# ----------------------------------------------------------------
def main():
    LOG_FILENAME = 'test.log'


    logger = logging.getLogger("SupervisordMonitor")
    logger.setLevel(logging.DEBUG)
    # create the logging file handler
    fh = logging.FileHandler(LOG_FILENAME)
    formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add handler to logger object
    logger.addHandler(fh)
    logger.info('------ Starting --------')

    manager(logger)

# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    main()
