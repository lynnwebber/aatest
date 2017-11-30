#!/usr/bin/python
#

import sys

from opcua import Client

def main():
    #client = Client("opc.tcp://kepserver1.wellkeeper.info:49320/OPCUA/SimulationServer")
    client = Client("opc.tcp://kepserver1.wellkeeper.info:49320")
    try:
	print 'about to connect'
        client.connect()
	print '  getting root node'
        root = client.get_root_node()
        print("Root Node:", root)
        print("Root Name:", root.get_browse_name())
        print("Children:", root.get_children())

	print '---> testing update on tag 1i (type Real/Float)'
	tag1 = client.get_node("ns=2;s=aaLandKTest.williston.testReal")
	print("tag1 is: {0} with value {1} ".format(tag1, tag1.get_value()))
	t1val = tag1.get_value()
	t1vtype = tag1.get_data_type_as_variant_type()
	t1new = t1val + 0.1
	#print("debug t1new:",t1new)
	tag1.set_data_value(t1new,varianttype=t1vtype)
	print("tag1 is: {0} with value {1} ".format(tag1, tag1.get_value()))

	print '---> testing update on tag 2 (type Boolean)'
	tag2 = client.get_node("ns=2;s=aaLandKTest.williston.testBool")
	print("tag2 is: {0} with value {1} ".format(tag2, tag2.get_value()))
	t2val = tag2.get_value()
	t2vtype = tag2.get_data_type_as_variant_type()
	if t2val is False: t2new = 1
	if t2val is True: t2new = 0
	#print("debug t2new:",t2new)
	tag2.set_data_value(t2new,varianttype=t2vtype)
	print("tag2 is: {0} with value {1} ".format(tag2, tag2.get_value()))

	print '---> testing update on tag 3 (type Int/Word)'
	tag3 = client.get_node("ns=2;s=aaLandKTest.williston.testInt")
	print("tag3 is: {0} with value {1} ".format(tag3, tag3.get_value()))
	t3val = tag3.get_value()
	t3vtype = tag3.get_data_type_as_variant_type()
	t3new = t3val + 1
	#print("debug t3new:",t3new)
	tag3.set_data_value(t3new,varianttype=t3vtype)
	print("tag3 is: {0} with value {1} ".format(tag3, tag3.get_value()))

    finally:
        client.disconnect()


# ---------- run main -------------
if __name__ == "__main__":
    main()

