#!/bin/bash

python3 first-scrape.py

sleep 5s

python3 re-filter.py

sleep 15s

python3 second-scrape.py

sleep 15s

python3 link-list-filter-regex.py

sleep 15s

python3 response.py