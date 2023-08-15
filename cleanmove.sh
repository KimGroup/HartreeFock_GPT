#!/bin/bash

# Get the current working directory
dir=$(pwd)

# Loop through all .tex files
for file in *.tex; do
    # Extract folder name without the extension
    foldername="${file%.*}"

    # Check if the folder exists
    if [[ ! -d "$foldername" ]]; then
        # If the folder doesn't exist, create it
        mkdir "$foldername"
    fi

    # Move the .tex file into the folder
    mv "$file" "$foldername/$file"
done
