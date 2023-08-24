#!/bin/bash

# This is a small script to render all the tex files into pdfs. 
# The script traverses all the folders and subfolders recursively and renders each tex file into a pdf using the shell of the system
# Input: None
# Output: .pdf files from each dot file

# Function to recursively process directories and files
process_directory() {
    dir="$1"
    blacklist=("defaults") # List of folders to skip

    for file in "$dir"/*; do
        if [[ -d "$file" ]]; then
            base_name=$(basename "$file")
            if [[ " ${blacklist[*]} " != *" $base_name "* ]]; then
                process_directory "$file"
            else
                echo "Skipping blacklisted folder: $file"
            fi
        elif [[ -f "$file" && "$file" =~ \.tex$ ]]; then
            echo "Compiling $file..."
		    pdflatex -interaction=nonstopmode -output-directory="$dir" "$file"
        fi
    done
}

# Start processing from the current directory
process_directory "."

echo "PDF compilation complete."

