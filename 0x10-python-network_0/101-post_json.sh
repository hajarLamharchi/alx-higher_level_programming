#!/bin/bash
# This script is documented
curl -s -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
