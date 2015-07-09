/*
 * all the handlers for the various restful calls
 */
package handlers

import (
	"fmt"
	"github.com/zenazn/goji/web"
	"io"
	"net/http"
)

// sends back a simple pong reply to the request
func Ping(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "PONG\n")
}

// sends back the current version number
func Version(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Current Version: %s \n", "V1.r0")
}

// posts the rtu_channel id to the specified nsq topic
//  checks first to verify that the rtu_channel exists
func RtuChannelNotice(c web.C, w http.ResponseWriter, r *http.Request) {
	id := c.URLParams["id"]
	fmt.Fprintf(w, "debug: checking for valid rtu_channel: %s\n", id)
	fmt.Fprintf(w, "debug: posting to NSQD: %s\n", id)
}
