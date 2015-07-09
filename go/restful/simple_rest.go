/*
  a simple restful server
*/
package main

import (
	"./handlers"
	"github.com/zenazn/goji"
	"net/http"
)

func main() {
	goji.Get("/", http.RedirectHandler("/ping", 301))
	goji.Get("/ping", handlers.Ping)
	goji.Get("/version", handlers.Version)
	goji.Get("/rtu_channel/notice/:id", handlers.RtuChannelNotice)
	goji.Serve()
}
