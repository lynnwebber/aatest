#!/usr/bin/python
#

import sys

from opcua import Client

def main():
    client = Client("opc.tcp://kepserver1.wellkeeper.info:49320")
    try:
        client.connect()
        root = client.get_root_node()
        print("Root Node:", root)
        print("Children:".root.get_children())
    finally:
        client.disconnect()


# ---------- run main -------------
if __name__ == "__main__":
    main()

