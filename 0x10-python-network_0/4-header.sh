#!/bin/bash
# GET and displays response body, adding header variable with parameter
curl -s "$1" -X GET -H "X-School-User-Id: 98"
