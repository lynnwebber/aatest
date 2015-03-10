Modbus Write Service

Functional Requirements:
    This service will receive input form a web based application that will
    format an XML-RPC record and call this service.
    
    It will take the input of the XML-RPC call, which contains an IP address,
    and information to write to a modbus register.

    Once called the service will make a connection to the device at the IP
    address and pass the modbus write information based on the protocol found
    in the documentation on: 
    http://tiger.wellkeeper.com/wiki/Wellkeeper/Projects/RemoteControl

    The information passed will be an xml document formatted as seen in the
    following example
    
    

    Note: was hoping to use json but it is not implemented until 2.6 as part of the python
    standard library.

This service uses XML-RPC as its input communication methodology on the following:

  Protocol: TCP/IP
  Port: 31031

To install:


To start: (by hand)


To configure automatic startup:


