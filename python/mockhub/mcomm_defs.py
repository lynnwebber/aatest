#!/usr/bin/python

'''
common definitions

Change the host name to use different server

10/07/2013.. initial release to test Lynn's value filter utility --JZ
'''

#hammerhead
#host = "155.229.187.12" 
host = "hammerhead.wellkeeper.com"

#production 
#host='207.114.199.57'
#host = 'reporting.wellkeeper.com'

# local host JZ_TEST
##host = 'localhost'

#amazon
#host='23.21.159.112'

version = '601E'

config_port = 44821
timeout = 8

config_prefix = '/var/volatile/'
data_prefix = '/media/card/'

config_id_file = config_prefix + 'current.cfg'
#config_fail_file = config_prefix + 'fail.cfg'
NULL_CONFIG=0xFFFFFFFF
HEADER_LEN=12
CKSM_LEN=2

modem_reset_timestamp='/var/volatile/modem.txt'

read_result_file_prefix = config_prefix
current_result_file = read_result_file_prefix + 'current.rst'

good_report_file = config_prefix + 'ok.snd'
count_in_file = '/tmp/count_in'
count_out_file = '/tmp/count_out'

env_filename='/var/volatile/cell_env.txt'

# MODBUS error code (hex)
MB_ERROR_MAJOR='00'
MB_TIMEOUT='80'
MB_RX_ERROR='81'
MB_TX_ERROR='82'
MB_INVALID_PARAMETER='84'
MB_ERROR_NORESULT='EF'
MB_ERROR_UNKNOWN='FF'

# config errors
CONFIG_ERROR_MAJOR='FF'
CONFIG_INVALID_TYPE ='01'
CONFIG_INVALID_PARAMETER='02'

# analog defines
MAX_ANALOG = 4
MIN_ANALOG = 1
ANALOG_PREFIX = 'adc'
ANALOG_ERROR = 'FFFFFFFF'

ANALOG_ERROR_MAJOR='02'
ANALOG_ERROR_NORESULT='EF'

# binary defines
MAX_BINARY = 8
MIN_BINARY = 1
BINARY_PREFIX = 'din'
BINARY_ERROR = 'FF'

BINARY_ERROR_MAJOR='03'
BINARY_ERROR_NORESULT='EF'

# modbus command support
MB_READ_COIL=1
MB_READ_INPUT=3
MB_READ_HOLD=4
MB_WRITE_COIL=5
MB_WRITE_REG=6

WK_CMD_FILE_DIR = '/var/volatile/cmd/'
#WK_CMD_FILE_DIR = '/home/julie/work/notes/test/ocd/python/cmd/'
WK_CMD_LOG = '/var/volatile/wkcmd.log'
