aws dynamodb create-table \
    --table-name readings \
    --attribute-definitions \
        AttributeName=measurement_tag_id,AttributeType=S \
        AttributeName=timestamp,AttributeType=N \
    --key-schema AttributeName=measurement_tag_id,KeyType=HASH AttributeName=timestamp,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --endpoint-url http://localhost:8000
