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


class debugCache:

    def __init__(self):
        self.facs = ''
        self.styles = ''

    def purge(self): self.__init__()

    # -----------------------------------------------------------
    def init_facs(self):
        self.facs = et.Element('factors')

    def put_fac(self,fn,val=''):
        if not self.facs: self.init_facs()
        x = et.SubElement(self.facs,fn)
        if val:
            x.text = str(val)

    def put_fac_child(self,fn,child,val=''):
        x = self.facs.find(fn)
        if x is None:
            raise IndexError, "Factor %s not found" % (fn)
        else:
            z = et.SubElement(x,child)
            if val:
                z.text = str(val)

    def get_facs_str(self): return et.tostring(self.facs)

    # -----------------------------------------------------------
    def init_styles(self):
        self.styles = et.Element('styles')

    def put_style(self,sn,val=''):
        if not self.styles: self.init_styles()
        x = et.SubElement(self.styles,sn)
        if val:
            x.text = str(val)

    def put_style_child(self,sn,child,val=''):
        x = self.styles.find(sn)
        if x is None:
            raise IndexError, "Style %s not found" % (sn)
        else:
            z = et.SubElement(x,child)
            if val:
                z.text = str(val)

    def get_styles_str(self): return et.tostring(self.styles)

debug = debugCache()

    
# ----------------------------------------------------------------
# main program module
#
def debugging_main():
    print "factor scoring cache/debugging module"


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__": debugging_main()
