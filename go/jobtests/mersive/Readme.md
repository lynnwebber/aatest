# Minimal HTTP Server

## Build Environment

* Requires Go compiler
* Requires bash shell for testing script
* Requires GNU make 

## Build and Run Instructions

The make utility can be used for all the build/run/test functions.

Building the server:
```
make build
```
Running the server:
```
make server-start
```
Note: when the server starts it will run in the forground.  To stop the server press Ctrl-c.

Testing the server:
```
make run-test
```
Note: this should be run in a different terminal session from the running server


## Design Summary
This server was designed to be very minimal in its functionality and only responds to three types of requests and to very simple input.  The basic outline of the processing is:
* Accept incomming messages on TCP port 8000.
* Parse the incomming HTTP request message pulling out the verb, the uri, content type and length from the header.  Place that data into a structure.
* Process the incomming request message
  * POST requests place an entry into the storage array 
  * GET requests look for a corresponding URI in the storage array and return the data from the posted message
  * DELETE requests look for a corresponding URI in the storage array and remove it from the array

For parsing simple string splitting was used to separate the different parts of the request.  This method was quick to develop but may not be adequate for more complex requests, especially the method of pulling the last line in the message as the body. See Improvements for more information.

For storage a simple array was used and is purged when the server is stopped.

## Improvements
Parsing the message body:
* a more robust method of extracting the message body would be needed if the body contains CRLF characters.

Storage:
* a storage method that has transactional integrity is really needed to support this applicaiton, although the server itself is concurrent by using go routines, the storage array is not and could cause a race condition under load

## Performance Concerns
* As noted in Improvements the storage method needs to be able to support concurrent message handling with locking features.

