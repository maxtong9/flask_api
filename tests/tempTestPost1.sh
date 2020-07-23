#!/bin/bash
curl -X POST --header "Content-Type:application/json" --data '{"temperature": -40.0, "unit" : "c" } ' http://localhost:5000/temperature