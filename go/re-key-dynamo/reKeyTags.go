package main

import (
	"encoding/csv"
	"errors"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"
	"github.com/aws/aws-sdk-go/service/dynamodb/dynamodbattribute"
	"github.com/spf13/viper"
)

var (
	inConfigFile string
	inRunMode    string
	rekeyFile    string
	appCfg       = new(appConfig)
)

func initFlags() {
	flag.StringVar(&inConfigFile, "config-file", "./config/reKeyTags.toml", "configuration file name (including path)")
	flag.StringVar(&inConfigFile, "c", "./config/reKeyTags.toml", "configuration file name (including path)")
	flag.StringVar(&inRunMode, "mode", "", "mode to run service (testing or production no default)")
	flag.StringVar(&inRunMode, "m", "", "mode to run service (testing or production no default)")
	flag.StringVar(&rekeyFile, "infile", "", "input text file containing old-tag-name|new-tag-names seperated by pipe symbol")
	flag.StringVar(&rekeyFile, "i", "", "input text file containing old-tag-name|new-tag-names seperated by pipe symbol")
}

type appConfig struct {
	Endpoint  string
	TableName string
}

// parse the configuration using viper and set the app information
//   based on the run mode flag from the command line
func (acfg *appConfig) Parse(inConfigFile string, inRunMode string) error {
	viper.SetConfigFile(inConfigFile)
	if err := viper.ReadInConfig(); err != nil {
		log.Println("could not read config")
		return err
	}
	temp := viper.Sub(inRunMode)
	if err := temp.Unmarshal(acfg); err != nil {
		log.Println("could not unmarshal config")
		return err
	}
	return nil
}

// Reading struct for readings from dynamodb readings table
type Reading struct {
	Tagid     string `json:"measurement_tag_id"`
	Timestamp int64  `json:"timestamp"`
	Value     string `json:"value"`
	Error     string `json:"error"`
}

// ------------------------------------------------------
func checkFlags() {
	if inConfigFile == "" {
		log.Fatal("--config-file is required")
	}

	if inRunMode == "" {
		log.Fatal("--mode is required")
	}

	if rekeyFile == "" {
		log.Fatal("--infile is required")
	}
}

// ------------------------------------------------------
func loadRekeyFile(rekeyFilename string) [][]string {

	file, err := os.Open(rekeyFilename)
	if err != nil {
		fmt.Println("\nProblem opening rekey input file - ", err.Error())
		os.Exit(1)
	}
	defer file.Close()

	r := csv.NewReader(io.Reader(file))
	r.Comma = '|'

	records, err := r.ReadAll()
	if err != nil {
		fmt.Println("Problem reading input rekey file - error:", err.Error())
	}
	return records
}

// ------------------------------------------------------
func readOldRecords(svc *dynamodb.DynamoDB, key string) []Reading {
	var rv = []Reading{}
	var queryInput = &dynamodb.QueryInput{
		TableName: aws.String(appCfg.TableName),
		KeyConditions: map[string]*dynamodb.Condition{
			"measurement_tag_id": {
				ComparisonOperator: aws.String("EQ"),
				AttributeValueList: []*dynamodb.AttributeValue{
					{
						S: aws.String(key),
					},
				},
			},
		},
	}

	resp, err := svc.Query(queryInput)
	if err != nil {
		fmt.Println("proglem reading old record", err.Error())
	} else {
		err = dynamodbattribute.UnmarshalListOfMaps(resp.Items, &rv)
		if err != nil {
			fmt.Printf("failed to unmarshall query result, %v", err)
		}
	}

	return rv
}

// ------------------------------------------------------
func addNewRecord(svc *dynamodb.DynamoDB, rdg Reading, newkey string) error {
	fmt.Println(rdg.Tagid, "--> ", newkey)
	rdg.Tagid = newkey
	amap, err := dynamodbattribute.MarshalMap(rdg)
	if err != nil {
		fmt.Println("Error marshaling new reading struct:", err.Error())
		return errors.New("addNewRecord - could not marshal reading with new key")
	}
	input := &dynamodb.PutItemInput{
		Item:      amap,
		TableName: aws.String(appCfg.TableName),
	}
	_, err = svc.PutItem(input)
	if err != nil {
		fmt.Println("Error calling PutItem: ", err.Error())
		return errors.New("addNewRecord - problem inserting new reading")
	}
	return nil
}

// ------------------------------------------------------
func delOldRecord(svc *dynamodb.DynamoDB, rdg Reading) error {
	fmt.Println("Removing: ", rdg.Tagid)
	ts := strconv.FormatInt(rdg.Timestamp, 10)
	input := &dynamodb.DeleteItemInput{
		Key: map[string]*dynamodb.AttributeValue{
			"measurement_tag_id": {
				S: aws.String(rdg.Tagid),
			},
			"timestamp": {
				N: aws.String(ts),
			},
		},
		TableName: aws.String(appCfg.TableName),
	}
	_, err := svc.DeleteItem(input)
	if err != nil {
		fmt.Println("Error calling DeleteItem: ", err.Error())
		return errors.New("addOldRecord - problem removing old reading")
	}
	return nil
}

// ------------------------------------------------------
// TODO: add some sort of throttleing or split to two modes add/delete
func main() {
	initFlags()
	flag.Parse()
	checkFlags()

	if err := appCfg.Parse(inConfigFile, inRunMode); err != nil {
		log.Fatal("problem parsing configuration file: ", err.Error())
	}

	// get the rekey data file
	rekeyData := loadRekeyFile(rekeyFile)

	// attach to dynamodb
	sess, err := session.NewSession(&aws.Config{
		Region:   aws.String("us-west-2"),
		Endpoint: aws.String(appCfg.Endpoint)},
	)
	if err != nil {
		fmt.Println("DynamoDB session error:", err.Error())
	}
	svc := dynamodb.New(sess)

	// pull the old and new key out of the input file and make the changes to 
	//  the dynamo table
	for _, rekeyrec := range rekeyData {
		oldKey := rekeyrec[0]
		newKey := rekeyrec[1]

		rdgs := readOldRecords(svc, oldKey)
		for _, rdg := range rdgs {
			if err := addNewRecord(svc, rdg, newKey); err != nil {
				fmt.Println("Problem adding record with new key: ", newKey, rdg.Timestamp)
			}
			if err = delOldRecord(svc, rdg); err != nil {
				fmt.Println("Problem removing record with old key: ", rdg.Tagid, rdg.Timestamp)
			}
		}
	}
}
