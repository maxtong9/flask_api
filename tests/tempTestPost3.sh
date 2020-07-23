#!/bin/bash
curl -X POST --header "Content-Type:application/json" --data '{"temperature": "Not A Number", "unit" : "f" } ' http://localhost:5000/temperature