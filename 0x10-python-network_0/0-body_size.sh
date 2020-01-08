#!/bin/bash
# cURL body size
curl -sI 0.0.0.0:5000 | awk '/Content-Length/ {print $2}' | cat -e