// a test go program for parsing alarm triggers
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
)

var cond interface{}

func expressionHandler(vv map[string]interface{}) {
	var okflag = false
	var funcflag = false
	if _, ok := vv["measurement_tag_id"]; ok {
		okflag = true
	}
	if _, ok := vv["function"]; ok {
		okflag = true
		funcflag = true
	}
	if okflag {
		if !funcflag {
			fmt.Printf("(%s (get_tag_value %s) %s)", vv["operation"], vv["measurement_tag_id"], vv["threshold"])
		} else {
			fmt.Printf("(%s (%s) %s)", vv["operation"], vv["function"], vv["threshold"])
		}
	}
}

// ------------------------------------------------
func processSexpr(tm map[string]interface{}) {
	for k, v := range tm {
		switch vv := v.(type) {
		case string:
			//fmt.Printf("%s --> %s --> %v \n\n", k, "string", v)
		case float64:
			//fmt.Printf("%s --> %s --> %v \n\n", k, "float64", v)
		case map[string]interface{}:
			if k == "condition" {
				fmt.Printf("(condition ")
				defer fmt.Printf(")")
			} else {
				expressionHandler(vv)
			}
			processSexpr(v.(map[string]interface{}))
		case []interface{}:
			if k == "and" {
				fmt.Printf("(and ")
				defer fmt.Printf(")")
			}
			if k == "or" {
				fmt.Printf("(or ")
				defer fmt.Printf(")")
			}
			for _, y := range vv {
				processSexpr(y.(map[string]interface{}))
			}
		case bool:
			//fmt.Printf("%s --> %s --> %v \n\n", k, "bool", v)
		case nil:
			//fmt.Printf("%s --> %s --> %v \n\n", k, "nil", v)
		default:
			fmt.Printf("%s --> %s --> %v \n\n", k, "unknown", v)
		}
	}
}

// --------------------------------------------------
func main() {
	fmt.Println(">>> testing json alarm_trigger decoding")

	infile, err := ioutil.ReadFile("./new_simple.json")
	if err != nil {
		fmt.Println("File error:", err)
		os.Exit(1)
	}

	json.Unmarshal(infile, &cond)

	zz := cond.(map[string]interface{})
	processSexpr(zz)

}
