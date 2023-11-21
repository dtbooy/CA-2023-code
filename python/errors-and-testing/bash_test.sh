#!/bin/bash

FILE=$1
echo $FILE

if [[ -f "$1" ]]; then
    echo "$1 exists.";
elif [[ -f "$2" ]]; then
    echo "$2 exists.";
fi
