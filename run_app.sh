#!/bin/bash

# Check if the input file exists
if [ ! -f devpost.txt ]; then
  echo "Error: devpost.txt file not found."
  exit 1
fi

# Loop through each line in the input file
while IFS= read -r domain; do
  # Run the app.py script with the current domain as input
  echo "$domain" | python app.py
done < devpost.txt
