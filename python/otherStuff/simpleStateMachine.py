#!/usr/bin/python
#

# A simple state machine using python function as "first class" functions
#   developed as test for custody xfer stuff

# states
#   wait_for_conn
#   rtu_checkin
#   process_rtu_checkin
#   send_custody_request
#   wait_for_rtu_ack

import time

def stateUpdate():
    pass

def wait_for_conn():
    print "waiting for a connection"
    time.sleep(10)
    print "   connection made - moving on to next state"
    stateUpdate = wait_for_rtu_checkin
    stateUpdate()

def wait_for_rtu_checkin():
    print "waiting for rtu checkin"
    time.sleep(3)
    print "   rtu checked in - moving on to next state"
    stateUpdate = process_rtu_checkin
    stateUpdate()

def process_rtu_checkin():
    print "processing the checin from the rtu"
    time.sleep(3)
    print "   processed - moving on"
    stateUpdate = send_custody_request
    stateUpdate()

def send_custody_request():
    print "sending custody request"
    time.sleep(3)
    print "   sent - moving on"
    stateUpdate = wait_for_ack
    stateUpdate()

def wait_for_ack():
    print "waiting for ack"
    time.sleep(3)
    print "   got an ack - start_over"

def main():
    print "starting up state machine and waiting for connection"
    while 1:
        wait_for_conn()

# -------------------------------------------------------------
if __name__ == "__main__":
    main()
