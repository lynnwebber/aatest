# Go parameters
GOCMD=go
GOBUILD=$(GOCMD) build
GOINSTALL=$(GOCMD) install
GOGET=$(GOCMD) get
SOURCE_NAME=reKeyTags.go
BINARY_NAME=reKeyTags
PRODCONFIG=/home/wellkeeper/config/

all: build

build: 
	$(GOBUILD) -o $(BINARY_NAME) $(SOURCE_NAME)

install: 
	$(GOINSTALL) $(SOURCE_NAME)

clean: 
	rm -f $(BINARY_NAME)

deps:
	$(GOGET) github.com/spf13/viper
	$(GOGET) github.com/aws/aws-sdk-go

prod-install:
	$(GOINSTALL) $(SOURCE_NAME)
	cp ./config/*.toml $(PRODCONFIG)

