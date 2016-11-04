#!/usr/bin/python
#
import os
import time as tm
import datetime as dt



def main():

    print "Starting"

    # get the current UTC time and print it formatted
    d = dt.datetime.utcnow()
    print 'Current UTC: ',dt.datetime.utcnow()

    # setup deltas 
    cst_diff = dt.timedelta(hours=6)
    mst_diff = dt.timedelta(hours=7)
    cst = d - cst_diff
    mst = d - mst_diff
    print 'Current CST: ',cst
    print 'Current MST: ',mst

    fmt = "%Y:%M:%d-%H:%M:%S"
    print 'UTC for REST Call: ',d.strftime(fmt)
   
    # convert specific time to UTC
    tday = dt.date.today()
    ttime = dt.time(07,0,0)
    target = dt.datetime.combine(tday,ttime)
    print target



# ------------------------------------------------------
if __name__ == "__main__":
    main()
