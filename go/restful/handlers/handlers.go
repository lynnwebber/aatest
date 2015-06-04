/*
 * all the handlers for the various restful calls
 */
package handlers

import (
    "fmt"
    "net/http"
    "github.com/zenazn/goji/web"
)

func Howdy(c web.C, w http.ResponseWriter, r *http.Request) {
    tname := c.URLParams["name"]
    fmt.Fprintf(w,"Howdy, %s \n",tname)
}
