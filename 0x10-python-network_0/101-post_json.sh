#!/bin/bash
# This script is documented
curl -d "$2" -H "Content-Type: application/json" -X POST "$1"
