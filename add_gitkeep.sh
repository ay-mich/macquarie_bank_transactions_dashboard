#!/bin/bash

# Find all directories in the current directory.
for d in $(find . -type d)
do
    # If the directory is empty...
    if [ -z "$(ls -A $d)" ]
    then
        # Add a .gitkeep file to it.
        touch "${d}/.gitkeep"
        echo "Added .gitkeep to empty directory: ${d}"
    fi
done
