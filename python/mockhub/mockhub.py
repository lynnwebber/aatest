#!/usr/bin/python

'''
Mock a hub

Usage: ./mockhub.py config_id report_interval

This script mock a hub, reading data from a file, config_id.data, where
config_id should be the id passed in.

The format of the file is: one item a line, anything that has a period, indicates a float, otherwise, an unsigned integer. However, a value is only read in
as a float if the configuration line asks for 4 bytes

If the number of lines in the data file is less than the number of data items
in the config, zero is used as the default value.

LIMITATION:
	Do not support signed integer

10/07/2013.. initial release to test Lynn's value filter utility --JZ
'''
import sys
import socket
import os
import struct
import array

import mcomm_defs
import mconfig_check

MAGIC_RPRT = 0x52505254

count_in = 0
count_out = 0

if len(sys.argv) < 3:
	print "Usage: ./mockhub.py config_id report_interval"
	sys.exit(1)

try:
	conf_id = int(sys.argv[1])
	rprt_intvl = int(sys.argv[2])
except:
	print "Failed to grab config id or report interval"
	sys.exit(1)

print "Will use configuration %d and report every %d seconds" %(conf_id, rprt_intvl)

# check whether data file exists
cfile = str(conf_id) + '.data'
if not os.path.exists(cfile):
	print "Cannot find the data file for config %d: %s" %(conf_id, cfile)
	sys.exit(1)

net_data = mconfig_check.build_pkt_cfg_download(conf_id)
print "Built config download pkt '%s'" %net_data

# download configuration
try:
	print "To init a socket"
	sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock2.settimeout(mcomm_defs.timeout)
	print "To connect to server"
	sock2.connect((mcomm_defs.host, mcomm_defs.config_port))
	print "To send to server"
	sock2.sendall(net_data)
	print "To receive from server"
	response = sock2.recv(2000)
	print "Got response length %d, type %r" %(len(response), type(response))


	sock2.close()

	config_content = response[:-2]
	print "config is \"%s\"" %config_content

	conf_lines = config_content.split('\n')

	#print "Got the following config lines:"
	#for line in conf_lines:
	#	print line
except:
	print "Failed to check the config %d" %conf_id
	sys.exit(1)

# parse the config

num_bytes = []

for line in conf_lines:
	line = line.lower()

	if line.startswith('param'):
		continue

	if line.startswith('modbus'):
		num_bytes.append(int(line.split()[-1]))
		continue

	if line.startswith('analog'):
		num_bytes.append(4)
		continue

	if line.startswith('binary'):
		num_bytes.append(1)

print "Got %d items, num bytes as %r" %(len(num_bytes), num_bytes,)

# read in data from data file

lines = []
try:
	fd = open(cfile, 'r')
	lines = fd.readlines()
	fd.close()
except:
	print "Cannot read %s for data items" %cfile

#parse data
items = []
num_items = len(num_bytes)
for i in range(num_items):
	if num_bytes[i] == 4:
		if lines[i].find('.') >= 0:
			# float
			try:
				value = float(lines[i])
			except:
				print "line '%s' cannot be converted to float" %lines[i]
				value = 0
			pkd = struct.pack('!f', value)
		else:
			try:
				value = int(lines[i])
			except:
				print "line '%s' cannot be converted to int" %lines[i]
			pkd = struct.pack('!I', value)

	elif num_bytes[i] == 2:
		try:
			value = int(lines[i][:lines[i].find('.')])
		except:
			print "line '%s' cannot be converted to int" %lines[i]
			value = 0
		pkd = struct.pack('!H', value)

	elif num_bytes[i] == 1:
		try:
			value = int(lines[i][:lines[i].find('.')])
		except:
			print "line '%s' cannot be converted to int" %lines[i]
			value = 0

		if value > 0:
			pkd = struct.pack('B', 1)
		else:
			pkd = struct.pack('B', 0)

	items.append(([pkd], num_bytes[i]))

print "data values got: "
total_len = 0
for item in items:
#	print "type of item %r, len of value %d" %(type(item), len(item[0][0]))
	total_len += len(item[0][0])
	print "%r" %(item,)

# make rprt packet
pkt = array.array('c', '\0' * (total_len * 2 + mcomm_defs.HEADER_LEN + mcomm_defs.CKSM_LEN + 50))
tmp_buf = array.array('c', '\0' * 10)
crc = 0
offset = 0

(pkt, offset, crc) = mconfig_check.mk_header(pkt, offset, tmp_buf, crc, MAGIC_RPRT)

# pack config id
struct.pack_into('!I', tmp_buf, 0, conf_id)
(pkt,offset, crc) = mconfig_check.pack_some(pkt, offset, tmp_buf, crc, 4)

# count in, then count out
struct.pack_into('!H', tmp_buf, 0, count_in)
(pkt,offset,crc) = mconfig_check.pack_some(pkt, offset, tmp_buf, crc, 2)

struct.pack_into('!H', tmp_buf, 0, count_out)
(pkt,offset,crc) = mconfig_check.pack_some(pkt, offset, tmp_buf, crc, 2)

# pack error bits

# number of error bytes
nbe = len(items) / 8
if len(items) % 8:
	nbe += 1

struct.pack_into('B', tmp_buf, 0, 0)

for i in range(nbe):
	(pkt, offset, crc) = mconfig_check.pack_some(pkt, offset, tmp_buf, crc, 1)

# pack data
for item in items:
	(pkt, offset, crc) = mconfig_check.pack_some(pkt, offset, item[0][0], crc, item[1])

# append crc
struct.pack_into('!H', tmp_buf, 0, crc)
(pkt, offset, crc) = mconfig_check.pack_some(pkt, offset, tmp_buf, crc, 2)

# TCP packet terminator
struct.pack_into('c', pkt, offset, '\xFF')
offset += 1
struct.pack_into('c', pkt, offset, '\x00')
offset += 1

# send packet
try:
	print "To init socket"
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print "To connect to host %s" %mcomm_defs.host
	sock.connect((mcomm_defs.host, mcomm_defs.config_port))
	print "To send"
	sock.sendall(pkt[:offset])
	print "To close"
	sock.close()
except:
	print "Failed to send data to server"


