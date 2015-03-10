#!/usr/bin/env python
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
import xml.etree.ElementTree as et

class scoresCache:

    def __init__(self):
        self.facs = ''
        self.styles = ''

    def purge(self): self.__init__()

    # -----------------------------------------------------------
    def init_facs(self):
        self.facs = et.Element('factors')

    def put_fac(self,fn):
        if not self.facs: self.init_facs()
        x = et.SubElement(self.facs,fn)
    
    def put_fac_info(self,fn,lst):
        x = self.facs.find(fn)
        if x is None:
            raise IndexError, "Factor %s not found" % (fn)
        else:
            for nam,val in lst:
                x.set(nam,str(val))

    def get_facs_str(self): return et.tostring(self.facs)

    # -----------------------------------------------------------
    def init_styles(self):
        self.styles = et.Element('styles')

    def put_style(self,sn):
        if not self.styles: self.init_styles()
        x = et.SubElement(self.styles,sn)
    
    def put_style_info(self,sn,lst):
        x = self.styles.find(sn)
        if x is None:
            raise IndexError, "Style %s not found" % (sn)
        else:
            for nam,val in lst:
                x.set(nam,str(val))

    def get_styles_str(self): return et.tostring(self.styles)

score = scoresCache()

    
# ----------------------------------------------------------------
# main program module
#
def scoring_main():
    print "factor scoring cache/scoring module"


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__": scoring_main()
