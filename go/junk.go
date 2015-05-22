// a test go program
package main

import "fmt"

func find_low(ary []int) int {
    rv := ary[0]
    for _,val := range ary {
        if val < rv {
            rv = val
        }
    }
    return rv
}

func find_high(ary []int) int {
    rv := ary[0]
    for _,val := range ary {
        if val > rv {
            rv = val
        }
    }
    return rv
}


func main() {
    var (
        x = []int{ 48,96,86,68, 57,82,63,70, 37,34,83,27, 19,97, 9,17}
        z = 0
    )
    z = find_low(x)
    fmt.Println("low: ",z)
    z = find_high(x)
    fmt.Println("high: ",z)
}
