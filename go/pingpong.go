// test of channels
package main


import (
    "fmt"
    "time"
    "math/rand"
    )

func pinger(c chan<- string) {
    for i := 1; i > 0 ; i++ {
        c <- "ping"
    }
}

func pong(c chan<- string) {
    for i := 0; ; i++ {
        c <- "  pong"
    }
}

func printer(c <-chan string) {
    for {
        fmt.Println(<-c)
        amt := time.Duration(rand.Intn(250))
        time.Sleep(time.Millisecond * amt)
    }
}

func main() {
    var c chan string = make(chan string)

    go pinger(c)
    go pong(c)
    go printer(c)

    var inp string
    fmt.Scanln(&inp)
}
