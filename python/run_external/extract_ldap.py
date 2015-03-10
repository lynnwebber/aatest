#!/usr/bin/python
#

import os
import glob
import datetime
import config as cfg
from ftplib import FTP

def set_fn():
    if cfg.opt.gen_filename:
        now=datetime.datetime.now()
        mon = str(now.month)
        dat = str(now.day)
        yr = str(now.year)
        hr = str(now.hour)
        mn = str(now.minute)
        fn = cfg.fn.fn_seed+"_"+mon+dat+yr+"_"+hr+mn+cfg.fn.ftype
    else:
        fn = cfg.fn.fn_seed+cfg.fn.ftype

    if cfg.opt.verbose: print "   Set new file name to: ",fn
    return fn


def remove_previous_files():
    if cfg.opt.remove_previous:
        for fn in glob.glob(os.path.join(os.getcwd(),cfg.prev.remove_fn)):
            os.remove(fn)
            if cfg.opt.verbose: print "   Removed old file: ",fn


def run_command(cmd,outfile):
    fullcmd = cmd+" > "+outfile
    if cfg.opt.verbose: print "   Running system command: ",fullcmd
    os.system(fullcmd)


def check_for_output(outfile):
    return os.path.exists(os.path.join(os.getcwd(),outfile))


def send_ftp(fn):
    if cfg.opt.verbose: print "   Sending FTP"
    ftp = FTP(cfg.ftp.host, cfg.ftp.user, cfg.ftp.pwd)
    fobj = open(fn,'rb')
    storcmd = "STOR %s" % fn
    ftp.storbinary(storcmd,fobj)
    fobj.close()
    ftp.quit()


def main():
    if cfg.opt.verbose: print "Extract LDAP Script Starting..."
    newfn = set_fn()
    remove_previous_files()
    run_command(cfg.pull.cmd,newfn)
    if check_for_output(newfn):
        if cfg.opt.verbose: print "   Output file found ready to send FTP..."
        send_ftp(newfn)
    else:
        msg = " ERROR - Could not find output file: %s " % newfn
        print msg
    if cfg.opt.verbose: print "Script complete" 


# -------------------------------------------------------------
if __name__ == "__main__":
    main()

