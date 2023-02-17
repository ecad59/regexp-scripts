#!/bin/bash

URL=""
NAME=""

while [[ ! `curl -s -o response.txt -w "%{http_code}" $URL` -eq "200" ]]; do
    echo "Waiting for $NAME to start ..."
    sleep 10
    continue
done

echo "$NAME successfully started."
rm response.txt -f