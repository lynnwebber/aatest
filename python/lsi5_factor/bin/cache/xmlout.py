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

import xml.etree.ElementTree as et
import scoring as scr
import debugging as dbg
import dimscores as ds

def gen_outstream():

    root = ds.xml.dstree
    
    scores = root.find('scores')
    scores.append(scr.score.facs)
    scores.append(scr.score.styles)
    
    debug = root.find('debugging')
    debug.append(dbg.debug.facs)
    debug.append(dbg.debug.styles)

    return et.tostring(root)
    
    
# ----------------------------------------------------------------
# main program module
#
def xmlout_main():
    print "doi scoring cache/xmlout module"


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__": xmlout_main()
