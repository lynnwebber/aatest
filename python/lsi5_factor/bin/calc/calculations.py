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

# imports
import os
import norms
import dimscores as ds
import config as cfg
import cache
from operator import itemgetter

# ----------------------------------------------------------------
class leadership_style:

    def __init__(self):
        self.faclist = []

    def add_factor(self,fac,opp,score):
        if score == 50.0:    
            self.faclist.append((fac,0))
        elif score > 50:
            strength = abs(score - 50)
            self.faclist.append((fac,strength))
        elif score < 50:
            strength = abs(50 - score)
            self.faclist.append((opp,strength))

    def get_style(self):
        lst = sorted(self.faclist,key=itemgetter(1),reverse=True)
        style = "%s:%s" % (lst[0][0],lst[1][0])
        return style

    def purge(self): self.__init__()

    # add calculation function (also add corresponding cache stuff)

ldrstyle = leadership_style()

# ----------------------------------------------------------------
def standardize(value,mean,stddev):
    stdscore = (((value - mean)/stddev) * cfg.stdweight) + cfg.stdconst
    return stdscore

# ----------------------------------------------------------------
def calc_factor_score(attrlst,facdims,fmean,fstddev):
    rv = ''
    # pull out the list of scores for this factor and average them
    #
    fdifflst = [y for x,y in attrlst if x in facdims]
    fdiffavg = ( sum(fdifflst) / float(len(fdifflst)) )
    #
    # standarsize the factor differential average to get the factor score
    #
    fscore = standardize(fdiffavg,fmean,fstddev)
    #
    # setup the debug information and return
    # 
    flds = 'facscore diffavg diffscores'.split()
    dat = [fscore,fdiffavg,fdifflst]
    dbg = zip(flds,dat)
    rv = [fscore,dbg]
    return rv

# ----------------------------------------------------------------
def calc_factors():
    facobj = norms.lsi5
    flist = facobj.get_list()

    for fac in flist:
        # get all the information for the factor (as dict)
        #
        f = facobj.get_as_dict(fac)
        if f['calctype'].lower() == 'std_score_avg':
            #
            # setup to place this info into the dim scores xml file
            #
            cache.score.put_fac(fac)
            cache.debug.put_fac(fac)
            #
            # calculate the score for this factor 
            #
            avgscore,dbgdat = calc_factor_score(ds.xml.dimlist,f['facdims'],f['mean'],f['stddev'])
            #
            # put the data out to the score portion of the xml document
            #
            fdata = []
            fdata.append(('score',avgscore))
            fdata.append(('opp',f['facop']))
            # format up the dimension stuff as right:left pairs for use
            #  in the reporting module
            t1 = f['facdims']
            t2 = zip(t1[::2],t1[1::2])   # break the flat list into tuple pairs
            t3 = [x+':'+y for x,y in t2]  # back to flat list with delimiter
            fdata.append(('dimensions','|'.join(t3)))
            # now store all the factor stuff
            cache.score.put_fac_info(fac,fdata)
            #
            # put the debugging data to the debug portion of the xml doc
            #
            cache.debug.put_fac_child(fac,'opp',f['facop'])
            cache.debug.put_fac_child(fac,'calc_type',f['calctype'])
            cache.debug.put_fac_child(fac,'calc_info',dbgdat)
            # 
            # add this score to the leadership style for calculation
            # 
            ldrstyle.add_factor(fac,f['facop'],avgscore)


# ----------------------------------------------------------------
def calc_styles():
    style = ldrstyle.get_style()
    sname = 'leadership'
    #
    # put data in the score part of xml
    #
    cache.score.put_style(sname)
    sdata = []
    sdata.append(('ident',style))
    cache.score.put_style_info(sname,sdata)
    #
    # put debugging data
    #
    cache.debug.put_style(sname)
    cache.debug.put_style_child(sname,'ident',style)
    cache.debug.put_style_child(sname,'calc_info',ldrstyle.faclist)
    #
    # cleanup
    #
    ldrstyle.purge()

# ----------------------------------------------------------------
# main program module
def calculations_main():
    print "factor scoring calculations module"

# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    calculations_main()
