#!/usr/bin/env python
# -----------------------------------------------------------------
#    * NOTICE *           * NOTICE *             * NOTICE *
# -----------------------------------------------------------------
#  Copyright 2009 and beyond, neoPsy Systems
#  Copyright 2009 and beyond, Somerville Partners LLC.
#                       ALL RIGHTS RESERVED
#  ENFORCABLE UNDER COPYRIGHT LAW OF THE UNITED STATES OF AMERICA. 
#  Use, duplication, or disclosure of this software in part or in 
#  full is prohibited without the written concent of neoPsy Systems
#  or Somerville Partners LLC.
# -----------------------------------------------------------------
# 

# imports
import os
import xml.etree.ElementTree as et

# ----------------------------------------------------------------
def getdim_pndiff(tree):
    rv = []
    xpth = 'scores/attributes'
    el = tree.find(xpth)
    for x in list(el): 
        dim = x.tag
        pndiff = float(x.get("posnegdiff"))
        rv.append((dim,pndiff))

    return rv

# ----------------------------------------------------------------
class lsi_ds_xml_mgr:

    def __init__(self):
        self.dstree = ''
        self.dimlist = []

    def parse(self,xmlstr):
        try:
            self.dstree = et.fromstring(xmlstr)
            self.dimlist = getdim_pndiff(self.dstree)
            rv = True
        except:
            rv = False

        return rv
    
    def purge(self): self.__init__()


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
