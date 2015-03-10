#!/usr/bin/env python
# 

# imports
import os
import logging

logger = logging.getLogger('HUBCommSvc')


# ----------------------------------------------------------------
class lsi_ds_xml_mgr:

    def __init__(self):
        self.dstree = 'this is a string to print out'

    def write_stuff(self):
        logger.info('message from write_stuff')
        print self.dstree
    


xml = lsi_ds_xml_mgr()

# ----------------------------------------------------------------
# main program module

def dsparse_main():
    print "dimension scores module/dsparse module"


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    dsparse_main()
