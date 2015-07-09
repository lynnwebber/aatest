// a test go program for the alarm triggers
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

type Reading struct {
	Tagid  string `json:"measurementid"`
	Value  string `json:"value"`
	Error  string `json:"error"`
	Tstamp string `json:"timestamp"`
}

func main() {
	fmt.Println(">>> testing json alarm_trigger decoding")

	infile, err := os.Open("simple.json")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer infile.Close()

	fmt.Printf("Timestamp: %s\n", newRdg.Tstamp)
}
