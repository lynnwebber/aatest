#!/usr/bin/python
#

import os

# ----------------------------------------------------------------
def horiz_cylinder_volume_ft(h=0,diam=0):
    r = diam/2
    pi = 3.1416
    cuft = ((r ** 2) * pi) * h
    return cuft

def cuft_2_bbls_us(cuft):
    gal_us = cuft * 7.48
    bbls = gal_us * 0.023810
    return bbls


# ----------------------------------------------------------------
def calc_main():
    print "SHL 4 Municipal Tanks   11-14-2015 06:58 EST\n"

    curr = 30.375
    wt1 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT1'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt1,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 31.417
    wt2 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT2'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt2,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 28.750
    wt3 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT3'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt3,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 31.0
    wt4 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT4'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt4,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 31.917
    wt5 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT5'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt5,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 31.625
    wt6 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT6'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt6,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 31.667
    wt7 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT7'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt7,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 28.0
    wt8 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT8'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt8,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    calc_main()
