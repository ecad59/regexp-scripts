#!/bin/bash

INPUT=""
#INPUT="google.com"

REGEX=''
#REGEX='^[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]\.[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]$'

while [[ false ]]; do
    if [ -z "$1" ]; then
        read -p 'Domain: ' INPUT
    else
        INPUT="$1"
    fi
 
    if [[ $INPUT =~ $REGEX ]]; then
        break
    else
        #echo "please enter a valid Domain."
        echo "please enter a valid INPUT"
        continue
    fi
done