#!/usr/bin/env python
 
"""
Configuration check

Modified from Portal's config_check.py

10/07/2013.. initial release to test Lynn's value filter utility --JZ
"""
 
import socket
import sys
import time
import struct
import array
import os

import mcomm_defs

# configure the client

#hammerhead
#host = "155.229.187.12" 
#host = "hammerhead.wellkeeper.com"

#production 
#host='207.114.199.57'
#host = 'customer.wellkeeper.com'

# local host JZ_TEST
##host = 'localhost'

#amazon
#host='23.21.159.112'

#print "Got host as \"" + host + "\""
 
#config_port = 44821
#timeout = 8

#version = '001C'
config_version = '\01'

# system dependent
#config_prefix = '/var/volatile/'
#data_prefix = '/media/card/'

#HEADER_LEN=12
CONFIG_LEN=4
PHONE_LEN=10
#CKSM_LEN=2
#ESCAPE_PROVISION=100
ESCAPE_BYTE = '\xFF'
RM_END = '\x00'
ESCAPE_PROVISION=40
MUID_LEN = 10
SERIAL_MIN_LEN = 3
VENDOR_MIN_LEN = 3
#NULL_CONFIG = 0xFFFFFFFF

MAGIC_CONF = 0x434F4E46

table = ( 
  0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50A5, 0x60C6, 0x70E7, 0x8108, 0x9129, 0xA14A, 0xB16B, 0xC18C, 0xD1AD, 0xE1CE, 0xF1EF,
  0x1231, 0x0210, 0x3273, 0x2252, 0x52B5, 0x4294, 0x72F7, 0x62D6, 0x9339, 0x8318, 0xB37B, 0xA35A, 0xD3BD, 0xC39C, 0xF3FF, 0xE3DE,
  0x2462, 0x3443, 0x0420, 0x1401, 0x64E6, 0x74C7, 0x44A4, 0x5485, 0xA56A, 0xB54B, 0x8528, 0x9509, 0xE5EE, 0xF5CF, 0xC5AC, 0xD58D,
  0x3653, 0x2672, 0x1611, 0x0630, 0x76D7, 0x66F6, 0x5695, 0x46B4, 0xB75B, 0xA77A, 0x9719, 0x8738, 0xF7DF, 0xE7FE, 0xD79D, 0xC7BC,
  0x48C4, 0x58E5, 0x6886, 0x78A7, 0x0840, 0x1861, 0x2802, 0x3823, 0xC9CC, 0xD9ED, 0xE98E, 0xF9AF, 0x8948, 0x9969, 0xA90A, 0xB92B,
  0x5AF5, 0x4AD4, 0x7AB7, 0x6A96, 0x1A71, 0x0A50, 0x3A33, 0x2A12, 0xDBFD, 0xCBDC, 0xFBBF, 0xEB9E, 0x9B79, 0x8B58, 0xBB3B, 0xAB1A,
  0x6CA6, 0x7C87, 0x4CE4, 0x5CC5, 0x2C22, 0x3C03, 0x0C60, 0x1C41, 0xEDAE, 0xFD8F, 0xCDEC, 0xDDCD, 0xAD2A, 0xBD0B, 0x8D68, 0x9D49,
  0x7E97, 0x6EB6, 0x5ED5, 0x4EF4, 0x3E13, 0x2E32, 0x1E51, 0x0E70, 0xFF9F, 0xEFBE, 0xDFDD, 0xCFFC, 0xBF1B, 0xAF3A, 0x9F59, 0x8F78,
  0x9188, 0x81A9, 0xB1CA, 0xA1EB, 0xD10C, 0xC12D, 0xF14E, 0xE16F, 0x1080, 0x00A1, 0x30C2, 0x20E3, 0x5004, 0x4025, 0x7046, 0x6067,
  0x83B9, 0x9398, 0xA3FB, 0xB3DA, 0xC33D, 0xD31C, 0xE37F, 0xF35E, 0x02B1, 0x1290, 0x22F3, 0x32D2, 0x4235, 0x5214, 0x6277, 0x7256,
  0xB5EA, 0xA5CB, 0x95A8, 0x8589, 0xF56E, 0xE54F, 0xD52C, 0xC50D, 0x34E2, 0x24C3, 0x14A0, 0x0481, 0x7466, 0x6447, 0x5424, 0x4405,
  0xA7DB, 0xB7FA, 0x8799, 0x97B8, 0xE75F, 0xF77E, 0xC71D, 0xD73C, 0x26D3, 0x36F2, 0x0691, 0x16B0, 0x6657, 0x7676, 0x4615, 0x5634,
  0xD94C, 0xC96D, 0xF90E, 0xE92F, 0x99C8, 0x89E9, 0xB98A, 0xA9AB, 0x5844, 0x4865, 0x7806, 0x6827, 0x18C0, 0x08E1, 0x3882, 0x28A3,
  0xCB7D, 0xDB5C, 0xEB3F, 0xFB1E, 0x8BF9, 0x9BD8, 0xABBB, 0xBB9A, 0x4A75, 0x5A54, 0x6A37, 0x7A16, 0x0AF1, 0x1AD0, 0x2AB3, 0x3A92,
  0xFD2E, 0xED0F, 0xDD6C, 0xCD4D, 0xBDAA, 0xAD8B, 0x9DE8, 0x8DC9, 0x7C26, 0x6C07, 0x5C64, 0x4C45, 0x3CA2, 0x2C83, 0x1CE0, 0x0CC1,
  0xEF1F, 0xFF3E, 0xCF5D, 0xDF7C, 0xAF9B, 0xBFBA, 0x8FD9, 0x9FF8, 0x6E17, 0x7E36, 0x4E55, 0x5E74, 0x2E93, 0x3EB2, 0x0ED1, 0x1EF0)

def getcrc_byte(bt, accum):
	#print "bt is type %r, value %r" %(type(bt), bt)
	tmp_bt = array.array('B', '\00')
	struct.pack_into('B', tmp_bt, 0, ord(bt))
	#print "tmp_bt has %02x" %(tmp_bt[0])
	accum = ((accum << 8) ^ table[(accum >> 8) ^ tmp_bt[0]]) & 0xFFFF
	return accum

# buf must be a char array
def getcrc(buf, length, accum):
	offset = 0
	while offset < length:
		#print "%d: %x accum %x" %(offset, buf[offset], accum)
		#print "index is %d, value %04x" %((accum >> 8) ^ buf[offset], table[(accum >> 8) ^ buf[offset]])
		#accum = ((accum << 8) ^ table[(accum >> 8) ^ buf[offset]]) & 0xFFFF
		accum = getcrc_byte(buf[offset], accum)
		offset += 1
	return accum

def calc_crc(buf, slen, accum):
	#print "Calculate crc with length %d" %slen

	while slen > 0:
		bytes = min(slen, 255)
		#print "Got bytes %d" %bytes
		accum = getcrc(buf, bytes, accum)
		buf = buf[bytes:]
		slen -= bytes

	return accum

def pack_byte_raw(buf, offset, bt, crc):
	struct.pack_into('c', buf, offset, bt)
	offset += 1
	if bt == ESCAPE_BYTE:
		struct.pack_into('c', buf, offset, '\xFF')
		offset += 1

	crc = getcrc_byte(bt, crc)
	return (buf, offset, crc)

def pack_some(pkt, offset, tmp_buf, crc, length):
	for i in range(length):
		(pkt, offset, crc) = pack_byte_raw(pkt, offset, tmp_buf[i], crc)
		
	return (pkt, offset, crc)

def mk_header(pkt, offset, tmp_buf, crc, magic):
	struct.pack_into('!I', tmp_buf, 0, magic)
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, 4)

	# major minor version
	struct.pack_into('!4s', tmp_buf, 0, mcomm_defs.version)
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, 4)

	# time
	struct.pack_into('!I', tmp_buf, 0, int(time.time()))
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, 4)

	return (pkt, offset, crc)

def build_pkt_cfg_check(muid, sr, vd):
	cfg_check = '\00'

	pkt_len = mcomm_defs.HEADER_LEN + CONFIG_LEN + len(muid)+len(sr) + len(vd) + ESCAPE_PROVISION

	offset = 0
	crc = 0
	pkt = array.array('c', '\0' * pkt_len)

	# temporary buffer for data conversion
	tmp_buf = array.array('c', '\0' * 50)

	(pkt, offset, crc) = mk_header(pkt, offset, tmp_buf, crc, MAGIC_CONF)

	# config version
	(pkt, offset, crc) = pack_byte_raw(pkt, offset, config_version, crc)

	# config check 
	(pkt, offset, crc) = pack_byte_raw(pkt, offset, cfg_check, crc)

	# area code
	area_code = muid[:3]
	struct.pack_into('!h', tmp_buf, 0, int(area_code))
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, 2)

	# local code
	local_number = muid[3:]
	struct.pack_into('!I', tmp_buf, 0, int(local_number))
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, 4)
	
	# vendor
	struct.pack_into('%ds' %(len(vd)), tmp_buf, 0, vd)
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, len(vd))
	
	# our software adds a null after vendor
	(pkt, offset, crc) = pack_byte_raw(pkt, offset, '\00', crc)

	# serial
	struct.pack_into('%ds' %(len(sr)), tmp_buf, 0, sr);
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, len(sr))

	#print "Length of packet: " + str(len(pkt)) + " added in " + str(offset)

	#print "Got crc as %x" %crc
	
	struct.pack_into('!H', tmp_buf, 0, crc)
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, 2)

	# TCP packet terminator
	struct.pack_into('c', pkt, offset, '\xFF')
	offset += 1
	struct.pack_into('c', pkt, offset, '\x00')
	offset += 1

	#i = 0
	#while i < offset:
	#	print "%d: %02x" %(i, ord(pkt[i]))
	#	i+= 1

	return pkt[:offset]

def build_pkt_cfg_download(conf_id):
	pkt_len = 50
	offset = 0
	crc = 0
	config_request = '\01'
	pkt = array.array('c', '\0' * pkt_len)

	# temporary buffer for data conversion
	tmp_buf = array.array('c', '\0' * 50)

	(pkt, offset, crc) = mk_header(pkt, offset, tmp_buf, crc, MAGIC_CONF)

	# config version
	(pkt, offset, crc) = pack_byte_raw(pkt, offset, config_version, crc)

	# config request 
	(pkt, offset, crc) = pack_byte_raw(pkt, offset, config_request, crc)

	# config id
	struct.pack_into('!I', tmp_buf, 0, conf_id)
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, 4)
	
	#print "final crc for config download %04x" %crc
	struct.pack_into('!H', tmp_buf, 0, crc)
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, 2)

	# TCP packet terminator
	struct.pack_into('c', pkt, offset, '\xFF')
	offset += 1
	struct.pack_into('c', pkt, offset, '\x00')
	offset += 1

	#i = 0
	#print "cfg download pkt, length %d" %offset
	#while i < offset:
	#	print "%d: %02x" %(i, ord(pkt[i]))
	#	i+= 1

	return pkt[:offset]

def build_config_accept(conf_id):
	pkt_len = 50
	offset = 0
	crc = 0
	config_accept = '\02'
	pkt = array.array('c', '\0' * pkt_len)

	# temporary buffer for data conversion
	tmp_buf = array.array('c', '\0' * 30)

	(pkt, offset, crc) = mk_header(pkt, offset, tmp_buf, crc, MAGIC_CONF)

	# config version
	(pkt, offset, crc) = pack_byte_raw(pkt, offset, config_version, crc)

	# config accept
	(pkt, offset, crc) = pack_byte_raw(pkt, offset, config_accept, crc)

	# config id
	struct.pack_into('!I', tmp_buf, 0, conf_id)
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, 4)

	# crc
	struct.pack_into('!H', tmp_buf, 0, crc)
	(pkt, offset, crc) = pack_some(pkt, offset, tmp_buf, crc, 2)

	# TCP packet terminator
	struct.pack_into('c', pkt, offset, '\xFF')
	offset += 1
	struct.pack_into('c', pkt, offset, '\x00')
	offset += 1

	#i = 0
	#print "cfg accept pkt, length %d" %offset
	#while i < offset:
	#	print "%d: %02x" %(i, ord(pkt[i]))
	#	i+= 1

	return pkt[:offset]

def save_config_id(conf_id):
	#print "to save config id as %d" %conf_id

	config_id_file_tmp = mcomm_defs.config_prefix + 'current.tmp'

	try:
		cf = open(config_id_file_tmp, 'w')
		cf.write('%d' %conf_id)
		cf.close()

		process = os.popen("mv %s %s" %(config_id_file_tmp, mcomm_defs.config_id_file))
		process.close()
	except:
		print "Cannot open config id tmp file to write"
		process = os.popen("rm -f %s" %config_id_file_tmp)	
		process.close()

def readin_value(filename):
	try:
		rf = open(filename, 'r')
		rst = rf.readline().strip()
		rf.close()
		return rst 
	except:
		return '\0'

def writeout_value(filename, value):
	try:
		rf = open(filename, 'w')
		rf.write(value)
		rf.close()
		return 1
	except:
		return 0

def mark_failure(fail_file):
	process = os.popen('touch %s' %fail_file)
	process.close()

def clear_failure(fail_file):
	process = os.popen('rm -f %s' %fail_file)
	process.close()

def has_config_failure():
	if os.path.exists(config_fail_file):
		print "Previous config check failed"
		return 1
	else:
		print "Previous config check successful"
		return 0

