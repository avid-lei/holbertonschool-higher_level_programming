#!/bin/bash
#curl display status code
curl -sI "$1" | awk '/HTTP/ {print $2}'
