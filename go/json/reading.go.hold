// a test go program
package main

import (
	"encoding/json"
	"fmt"
)

type Reading struct {
	Tagid  string `json:"measurementid"`
	Value  string `json:"value"`
	Error  string `json:"error"`
	Tstamp string `json:"timestamp"`
}

func main() {
	fmt.Println(">>> ready to test json decoding")
	var newRdg Reading
	sample := `{"MeasurementID":"123.22576.1","Value":"12.543","Error":"0","Timestamp":"2015/06/28 10:24:15 UTC","Alarm":"[1123.1436284713]"}`
	json.Unmarshal([]byte(sample), &newRdg)
	fmt.Printf("Tag: %s\n", newRdg.Tagid)
	fmt.Printf("Value: %s\n", newRdg.Value)
	fmt.Printf("Error: %s\n", newRdg.Error)
	fmt.Printf("Timestamp: %s\n", newRdg.Tstamp)
}
