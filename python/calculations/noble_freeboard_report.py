#!/usr/bin/python
#

import os

# --- calculation functions ------------------------------
# given height and diameter return volume in cubic feet
def horiz_cylinder_volume_cuft(h=0,diam=0):
    r = diam/2
    pi = 3.1416
    cuft = ((r ** 2) * pi) * h
    return cuft

# ---------------------------------------
# given cubic feet return gallons (US)
def cuft_2_gal_us(cuft):
    gal_us = cuft * 7.48
    return gal_us

# ---------------------------------------
# given gallons (US) return barrels (US)
def gal_us_2_bbls_us(gal_us):
    bbls = gal_us * 0.023810
    return bbls

# ---------------------------------------
#given cubic feet return barrels (US)
def cuft_2_bbls_us(cuft):
    gal_us = cuft * 7.48
    bbls = gal_us * 0.023810
    return bbls

# --- config and gather functions ------------------------------
def setup_config():
    a = [
        {"device":"123456","tags":["123.123456.1"]},
        {"device":"123456","tags":["123.123456.1"]},
        {"device":"123456","tags":["123.123456.1"]},
        {"device":"123456","tags":["123.123456.1"]},
        {"device":"123456","tags":["123.123456.1"]},
        {"device":"123456","tags":["123.123456.1"]},
        {"device":"123456","tags":["123.123456.1"]},
        {"device":"123456","tags":["123.123456.1"]}
        ]
    return a

def get_equip_info(tdict):
    pass




# ----------------------------------------------------------------
def main():
    # setup the equipment and measurement tags
    # pull equipment information
    # pull measurement tag reading data
    # calculate values
    # print


    print "SHL 4 Municipal Tanks   11-03-2015 06:56 EDT\n"

    curr = 30.333
    wt1 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT1'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt1,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 31.333
    wt2 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT2'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt2,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 28.625
    wt3 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT3'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt3,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 30.916
    wt4 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT4'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt4,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 31.791
    wt5 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT5'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt5,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 31.5
    wt6 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT6'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt6,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 31.541
    wt7 = cuft_2_bbls_us(horiz_cylinder_volume_ft(h=curr,diam=89.525))
    print 'WT7'
    print 'Capacity: 36995.97 BBLS'
    print 'Current Volume:',wt7,"BBLS"
    print 'Current Level:',curr,"ft"
    print 'Alarm Level: 31.69 ft\n'

    curr = 27.916
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
    main()
