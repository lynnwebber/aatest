import os, sys

import json 
import boto3
ddb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')

# -------------------------------------------------------------
def main():
    # connect to dynamodb2
    table = ddb.Table('readings')

    # parse the json file
    with open("readings_load.json") as infile:
        theData = json.load(infile)

    # insert the data
    for x in theData["loadData"]:
        table.put_item(Item=x)

# -------------------------------------------------------------
if __name__ == "__main__":
    main()
