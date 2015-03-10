#!/usr/bin/python
#
import logging


# -------------------------------------------------------------
def main():
    # basic setup
    logger = logging.getLogger("logtest.py")
    logger.setLevel(logging.INFO)
    lfh = logging.FileHandler("logging_test.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    lfh.setFormatter(formatter)
    logger.addHandler(lfh)

    print "*"*20," start logging stuff "
    
    logger.debug("debugging message")
    logger.info("informational message")
    logger.error("error message")

    print "*"*20," stop logging stuff "
# -------------------------------------------------------------
if __name__ == "__main__":
    main()
