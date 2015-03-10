#!/usr/bin/python
#

import os
import dimscores as ds

import logging


def atest_main():
    LOG_FILENAME = 'test.log'


    logger = logging.getLogger("HUBCommSvc")
    logger.setLevel(logging.DEBUG)
     
    # create the logging file handler
    fh = logging.FileHandler(LOG_FILENAME)
     
    formatter = logging.Formatter('%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
     
    # add handler to logger object
    logger.addHandler(fh)

    logger.info('------ Starting service --------')

    logger.info("this is a test of the my logger")

    ds.xml.write_stuff()


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    atest_main()
