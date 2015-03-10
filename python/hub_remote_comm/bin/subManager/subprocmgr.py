#!/usr/bin/env python

# imports
import os, sys
import subprocess 
import inputParser as ireq

def run_sub(instring):
    # pull target data out of input request
    tgt = ireq.reqdata.target
    typ = tgt['comm_type'].lower()
    # determine type and setup target client
    if typ == "modbus_write":
        sub_target_app = "python"
        sub_target_pgm = "udp_modbus_client.py"

    subprocess.Popen([sub_target_app,sub_target_pgm,instring])
    rv = True
    return rv

# ----------------------------------------------------------------
# main program module

def subprocmgr_main():
    print "sub process management module"


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    subprocmgr_main()
