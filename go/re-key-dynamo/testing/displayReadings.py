import os, sys

import json 
import boto3
from boto3.dynamodb.conditions import Key, Attr
ddb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')

# -------------------------------------------------------------
def main():
    # connect to dynamodb2
    table = ddb.Table('readings')

    # resp = table.query(
    #     KeyConditionExpression=Key('measurement_tag_id').eq('330.29250.1')
    # )
    resp = table.scan(
        FilterExpression=Attr('timestamp').gt(0)
    )
    for rec in resp['Items']:
        print (rec['measurement_tag_id'],rec['timestamp'],rec['value'],rec['error'])
# -------------------------------------------------------------
if __name__ == "__main__":
    main()
