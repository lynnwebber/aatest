// test program for go routines and channels
package main

import (
    "fmt"
    "time"
    "math/rand"
    )

func gr(n int) {
    for i := 0; i<10 ; i++ {
        fmt.Println("routine:",n,":",i)
        amt := time.Duration(rand.Intn(250))
        time.Sleep(time.Millisecond * amt)
    }
}

func main() {
    for i:=0; i<5; i++ {
        go gr(i)
    }
    var input string
    fmt.Scanln(&input)
}
