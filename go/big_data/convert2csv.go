/*
expected to take a file that was created by dumping a table from DynamoDB
into a JSON formatted records (one object per line) from the Wellkeeper
readings table
Convert it to csv format
*/
package main

import (
	"bufio"
	"encoding/csv"
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"os"
)

var (
	inFile  string
	outFile string
)

func initFlags() {
	flag.StringVar(&inFile, "infile", "", "input AWS json DynamoDB table dump file")
	flag.StringVar(&inFile, "i", "", "input AWS json DynamoDB table dump file")
	flag.StringVar(&outFile, "outfile", "", "output csv file name")
	flag.StringVar(&outFile, "o", "", "output csv file name")
}

// ReadingDump struct for readings from dynamodb readings dump
type ReadingDump struct {
	Tagid     AwsAttributeString `json:"measurement_tag_id"`
	Timestamp AwsAttributeNumber `json:"timestamp"`
	Value     AwsAttributeString `json:"value"`
	Error     AwsAttributeString `json:"error"`
}

// AwsAttributeString is a way to read the aws attribute string type
type AwsAttributeString struct {
	Data string `json:"s"`
}

// AwsAttributeNumber is a way to read the aws attribute string type
type AwsAttributeNumber struct {
	Data string `json:"n"`
}

// ------------------------------------------------------
func checkError(msg string, err error) {
	if err != nil {
		log.Fatal(msg, err)
	}
}

// ------------------------------------------------------
func checkFlags() {
	if inFile == "" {
		log.Fatal("--infile is required")
	}
	if outFile == "" {
		log.Fatal("--outfile is required")
	}
}

// ------------------------------------------------------
func processRecords(inFileName string, outFileName string) int64 {
	var (
		counter    int   = 0
		totalCount int64 = 0
	)
	// open the input file and create the file scanner
	file, err := os.Open(inFileName)
	checkError("Problem opening input file", err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	// open the output file and create the csv writer and a counter
	//  for the buffer write
	csvfile, err := os.Create(outFileName)
	checkError("Problem creating output file", err)
	defer csvfile.Close()

	writer := csv.NewWriter(csvfile)

	var rec ReadingDump
	for scanner.Scan() {
		counter = counter + 1
		rdg := []byte(scanner.Text())
		err := json.Unmarshal(rdg, &rec)
		checkError("Problem unmarshalling reading", err)

		csvdata := []string{rec.Tagid.Data, rec.Timestamp.Data, rec.Value.Data, rec.Error.Data}
		//csvstruct := [][]string{csvdata}
		err = writer.Write(csvdata)
		checkError("Problem writing to csv file", err)

		if counter >= 10 {
			writer.Flush()
		}
		totalCount = totalCount + 1
	}
	writer.Flush()
	return totalCount
}

// ------------------------------------------------------
func main() {
	initFlags()
	flag.Parse()
	checkFlags()

	// get the process the input file
	//TODO: have this routine return the number of records processed a
	//      and print out something nice
	tot := processRecords(inFile, outFile)
	fmt.Println("Conversion Complete:")
	fmt.Println("\tTotal records processed: ", tot)
	fmt.Println("\tOutput File: ", outFile)

}
