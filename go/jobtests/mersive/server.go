package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"strconv"
	"strings"
)

// global variables
//  verbose = true used to print output to terminal about server activities
//  storage is used to store an array of pointers to msgInfo items
var (
	verbose bool = false
	storage []*msgInfo
)

// constants used for http response messages
// the HTTP200V response message contains encodings for the type length and body
// it will be used when returning a GET request.
const (
	HTTP200  = "HTTP/1.1 200 OK\n"
	HTTP200V = "HTTP/1.1 200 OK\nContent-Type: %s \nContent-Length: %d \n\n%s"
	HTTP400  = "HTTP/1.1 400 Bad Request\n"
	HTTP404  = "HTTP/1.1 404 NotFound\n"
	HTTP500  = "HTTP/1.1 500 Internal Server Error\n"
)

// verbosePrint - prints the passed message if the verbose flag is true
func verbosePrint(a ...interface{}) {
	if verbose {
		log.Println(a...)
	}
}

// msgInfo will be used to hold the message information for valid messages
//  and possibly be used to store in an array for update and delete
type msgInfo struct {
	verb       string
	uri        string
	contentTyp string
	contentLen int
	body       string
}

// storageInsert - inserts a pointer into the array of pointers to items that
//  have been posted
func storageInsert(mip *msgInfo) (success bool) {
	storage = append(storage, mip)
	success = true
	return
}

// storageFind - find the msgInfo pointer that corresponds to the URI
//  for this request.  If found return the message pointer and true for
//  the success value
//  Otherwise - return nil for the pointer anf false for the success status
func storageFind(uri string) (foundMip *msgInfo, success bool) {
	foundMip = nil
	success = false
	for _, tMip := range storage {
		if tMip.uri == uri {
			foundMip = tMip
			success = true
			return
		}
	}
	return
}

// storageRemove - for the passed URI find the index of the matching msgInfo
//  pointer.
//  if found - copy the last item in the array to the current location then
//  shorten the array by one item and return true
//  if not found - return false as the success status
func storageRemove(uri string) (success bool) {
	found := false
	success = false
	idx := -1
	for i, tMip := range storage {
		if tMip.uri == uri {
			idx = i
			found = true
			break
		}
	}
	if found {
		storage[idx] = storage[len(storage)-1]
		storage = storage[:len(storage)-1]
		success = true
	}
	return
}

// processRequest looks at a message info structure to determine what to do with this
//  request message.
func processRequest(inMip *msgInfo) (response string) {
	switch inMip.verb {
	case "GET":
		inURI := inMip.uri
		outMip, found := storageFind(inURI)
		if !found {
			response = HTTP404
		} else {
			response = fmt.Sprintf(HTTP200V, outMip.contentTyp, outMip.contentLen, outMip.body)
		}
	case "POST":
		inserted := storageInsert(inMip)
		if !inserted {
			response = HTTP500
		} else {
			response = HTTP200
		}
	case "DELETE":
		inURI := inMip.uri
		removed := storageRemove(inURI)
		if !removed {
			response = HTTP500
		} else {
			response = HTTP200
		}
	case "NONE":
		response = HTTP400
	}
	return
}

// string2Lines - a quick function to pull the data line-by-line out of the
//   message buffer into an array of lines
func string2Lines(s string) (lines []string) {
	scanner := bufio.NewScanner(strings.NewReader(s))
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return
}

// parseMessage tries to pull the appropriate information from the message into a msgInfo
//   structure.  If the message is invalid an error will be returned and the state of the
//   acompanying structure cannot be guaranteed.  If the message is correctly parsed the
//   current information will be returned in the msgInfo structure and nil for error
func parseMessage(message string) (*msgInfo, error) {
	mi := msgInfo{verb: "NONE", uri: "NONE", contentTyp: "text/plain", contentLen: 0, body: " "}
	lines := string2Lines(message)
	for _, ln := range lines {
		tln := strings.TrimSpace(ln)
		lnarray := strings.Split(tln, " ")
		switch lnarray[0] {
		case "POST", "GET", "DELETE":
			mi.verb = lnarray[0]
			mi.uri = lnarray[1]
		case "Content-Type:":
			mi.contentTyp = lnarray[1]
		case "Content-Length:":
			mi.contentLen, _ = strconv.Atoi(lnarray[1])
		}
	}
	if mi.contentLen > 0 {
		lastLn := lines[len(lines)-1]
		mi.body = lastLn
	}
	return &mi, nil
}

// handleRequest receives a connection and the data passed in that connection
// from the caller, pulls it into a buffer (of bytes) converts it to a string
// message which is then parsed and handled
func handleRequest(conn net.Conn) {
	bufferBytes := make([]byte, 1024)
	_, err := conn.Read(bufferBytes)

	if err != nil {
		log.Println("Error reading request", err.Error())
		conn.Close()
		return
	}

	clientIP := conn.RemoteAddr().String()
	verbosePrint("Requesting Client IP:", clientIP)

	message := string(bufferBytes)
	mip, err := parseMessage(message)
	verbosePrint("Request msgInfo values: ", mip)

	response := processRequest(mip)

	verbosePrint("Storage item Count:", len(storage))
	verbosePrint("Response to Client:", response)

	conn.Write([]byte(response))
	conn.Close()

	verbosePrint(" ----- request completed ----- ")

}

// Main - Configures the port and protocol to listen
// Then makes the connection to the listner to accept connections and data
// when it receives a reqeust (of any sort) it initiates a go routine to handle the request
// This server should be highly concurrent (assuming enough memory).  The connection to the
// client is closed by the handler thus the server is free to accept more incomming messages.
func main() {
	listener, err := net.Listen("tcp", "127.0.0.1:8000")
	if err != nil {
		log.Fatal("tcp server listener error:", err)
	}

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatal("tcp server accept error", err)
		}
		verbosePrint(" ----- starting request ----- ")
		go handleRequest(conn)
	}
}
