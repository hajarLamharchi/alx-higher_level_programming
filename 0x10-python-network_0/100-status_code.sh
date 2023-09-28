#!/bin/bash
# This script return the status code only
curl -LI "$1" -o /dev/null -w '%{http_code}\n' -s
