/*
  a simple restful server
 */
package main

import (
    "log"
    "fmt"
    "time"
    "os"
    "os/signal"
    "syscall"
    "github.com/lib/pq"
)

func processPayload(n *pq.Notification) {
    fmt.Printf("  Payload: %s \n",n.Extra)
}


func main() {
    var conninfo string = "user=lynn dbname=lynn sslmode=disable"

    // setup a channel to catch operating system signals
    sigChan := make(chan os.Signal, 1)
    signal.Notify(sigChan, syscall.SIGINT, syscall.SIGTERM)

    // setting up listner callback function for problems
    reportProblem := func(ev pq.ListenerEventType, err error) {
        if err != nil {
            fmt.Println(err.Error())
        }
    }

    // setting up listner
    listener := pq.NewListener(conninfo, 10 * time.Second, time.Minute, reportProblem)
    err := listener.Listen("rtu_sync")
    if err != nil {
        log.Fatal(err)
    }
    defer listener.Close()

    fmt.Println("entering main listener loop")
    for {
        // start working on notifications
        select {
        case n := <- listener.Notify:
            fmt.Println("received notification from db")
            processPayload(n)
        case <- time.After(120 * time.Second):
            go func() {
                listener.Ping()
            }()
            //check to see if there is a notification or deal with
            //  connection loss and reconnect
            fmt.Println("nothing after 120 seconds, re-checking")
        case <- sigChan:
            fmt.Println("closing application")
            listener.UnlistenAll()
            return
        }
    }

}
