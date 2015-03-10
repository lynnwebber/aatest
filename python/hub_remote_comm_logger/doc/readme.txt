Hub Communications Logger

This service works in conjunction with the HUB Remote Communication 
service.  It is intended to log the information returned from the HUB
which will coencide with a server-to-hub communication.

Example:

	the server will send a request to the hub for a modbus write
	on port 44800.  As the hub processes the command it sends
	messages back to this service on port 44823.  These messages
	will contain information about handling and success/failure
	from the HUB.

	Example messages:
	   RCVD 1234
	   MODBUS 1234 SUCCESS
	   MODBUS 1234 FAILURE 0x04321

Functional Requirements:
	Service will receive simple UDP message, take the message
	content (no matter what it is) and post it to the log file.

This service uses simple UDP as its input communication methodology on the following:

  Protocol: UDP/IP
  Port: 44823


