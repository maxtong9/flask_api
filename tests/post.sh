#!/bin/bash

# Test the POST Request on the flask API Server

curl -X POST --header "Content-Type:application/json" --data '{ "email" : "steve@example.org", "number" : 1000 }' http://localhost:5000