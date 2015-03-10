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

import re
# ------------- 5 factor array offset information -----------------
# [rsl,mn,sd,lsl,ct,dms]
#  0   1  2  3   4  5  
#
rsl=0; mn=1; sd=2; lsl=3; ct=4; dml=5 

class lsiFactorNorms:

    def __init__(self,facfile="unknown"):

        self.normlist= []
        fobj = open(facfile,'r')
        for line in fobj:
            x = line.strip()
            y = x.split('|')
            # do all the castings at read time 
            y[mn] = float(y[mn])
            y[sd] = float(y[sd])
            # break dimensions (both prim and opposite) into a list
            y[dml] = re.split('[/:]',y[dml])
            self.normlist.append(y)
        fobj.close()

    def _get(self,fac):
        for x in self.normlist:
            if x[rsl] == fac.lower():
                return x
        return []
    
    def get_list(self):
        rv = []
        for x in self.normlist:
            rv.append(x[rsl])
        return rv

    def get_as_dict(self,fac):
        rv = {}
        names = 'fac mean stddev facop calctype facdims'.split()
        dat = self._get(fac)
        tmp = zip(names,dat)
        rv = dict(tmp)
        return rv

lsi5 = lsiFactorNorms("data-files/lsi_5factor.txt")

# ----------------------------------------------------------------
# main program module
#
def factors_main():
    print "lsi factor norms"


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    factors_main()
