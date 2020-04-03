# Go parameters
GOCMD=go
GOBUILD=$(GOCMD) build
SOURCE_NAME=server.go
BINARY_NAME=server

all: build

build: 
	$(GOBUILD) -o $(BINARY_NAME) $(SOURCE_NAME)

clean: 
	rm -f $(BINARY_NAME)

server-start:
	./$(BINARY_NAME)

run-test:
	bash tester.sh