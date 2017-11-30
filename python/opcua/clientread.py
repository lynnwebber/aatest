#!/usr/bin/python
#

import sys

from opcua import Client

def main():
    #client = Client("opc.tcp://kepserver1.wellkeeper.info:49320/OPCUA/SimulationServer")
    client = Client("opc.tcp://kepserver1.wellkeeper.info:49320")
    try:
	print 'about to connect to opc-ua'
        client.connect()
	print '  getting root node'
        root = client.get_root_node()
        print("Root Node:", root)
        print("Root Name:", root.get_browse_name())
        #print("Children:", root.get_children())

	tag1 = client.get_node("ns=2;s=StrongElectricDemo.SCADAPAC350.04")
	print("tag1 is: {0} with value {1} ".format(tag1, tag1.get_value()))
	t1val = tag1.get_value()
	t1vtype = tag1.get_data_type_as_variant_type()
	t1new = t1val + 0.1
	tag1.set_data_value(t1new,varianttype=t1vtype)
	print("tag1 is: {0} with value {1} ".format(tag1, tag1.get_value()))

    finally:
        client.disconnect()
	print 'opc-ua disconnected'


# ---------- run main -------------
if __name__ == "__main__":
    main()

