#!/bin/bash
curl -X POST --header "Content-Type:application/json" --data '{"temperature": 100.0, "unit" : "f" } ' http://localhost:5000/temperature