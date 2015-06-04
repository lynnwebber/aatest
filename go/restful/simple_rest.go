/*
  a simple restful server
 */
 package main

 import (
     "github.com/zenazn/goji"
     "./handlers"
 )

 func main() {
     goji.Get("/howdy/:name", handlers.Howdy)
     goji.Serve()
 }
