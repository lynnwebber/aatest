echo "bad request in verbose mode to see reply"
curl -v -d "bad request test" -X PUT http://localhost:8000/badrequest

echo -e "\n\ndoing foo - initial get expect 404"
curl -i http://localhost:8000/foo
echo -e "\nfoo - post expect 200"
curl -i -H "Content-Type: application/json" -X POST -d '{ "secret": 42 }' http://localhost:8000/foo
echo -e "\nfoo - get expect 200 with json output"
curl -i http://localhost:8000/foo

echo -e "\n\ndoing yo-yo - post expect 200"
curl -i -H "Content-Type: text/plain" -X POST -d 'squeamish ossifrage' http://localhost:8000/yo/yo/yo
echo -e "\nyo-yo - get expect 200 with text output"
curl -i http://localhost:8000/yo/yo/yo
echo -e "\nyo-yo - delete expect 200 "
curl -i -X DELETE http://localhost:8000/yo/yo/yo
echo -e "\nyo-yo - get expect 404 "
curl -i http://localhost:8000/yo/yo/yo

