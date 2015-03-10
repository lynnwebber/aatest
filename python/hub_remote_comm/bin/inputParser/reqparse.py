#!/usr/bin/env python

# imports
import os
import xml.etree.ElementTree as et


# ----------------------------------------------------------------
def getReqDict(tree,xpath):
    rv = []
    el = tree.find(xpath)
    for x in list(el): 
        fld = x.tag
        val = x.text
        rv.append((fld,val))

    return dict(rv)

# ----------------------------------------------------------------
class req_xml_mgr:

    def __init__(self):
        self.reqtree = ''
        self.target = ''
        self.mbwrite = {}

    def parse(self,xmlstr):
        try:
            self.reqtree = et.fromstring(xmlstr)
            self.target = getReqDict(self.reqtree,'target')

            if self.target["comm_type"].lower() == "modbus_write":
                self.mbwrite = getReqDict(self.reqtree,'mb_write')

            rv = True
        except:
            rv = False

        return rv
    
    def purge(self): self.__init__()


reqdata = req_xml_mgr()

# ----------------------------------------------------------------
# main program module

def reqparse_main():
    print "request parse module"


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    reqparse_main()
