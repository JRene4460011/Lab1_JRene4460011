#!/bin/bash
directory="archive"

# Check if the directory exists. Then if not, I'll create it.

if [ ! -d "$directory" ]; then
    mkdir "$directory"
    echo "Directory '$directory' created."
else
    echo "Directory '$directory' already exists."
fi

# I'll then create the timestamp representing the current date and time.
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
echo "Timestamp: $timestamp"

sleep 1

# The archival process
original_file="grades.csv"

if [ -f "$original_file" ]; then

    filename="${original_file%.*}"
    extension="${original_file##*.}"

    new_file="$directory/${filename}_$timestamp.$extension"

    if mv "$original_file" "$new_file"; then

        echo "File '$original_file' has been archived as '$new_file'."
    
        if touch grades.csv; then
            echo "A new empty 'grades.csv' file has been created!!!"
        else
            echo "Failed to create a new 'grades.csv' file!!"
        fi
    
    else
        echo "Failed to archive '$original_file'."
    fi

else

    echo "File '$original_file' does not exist. Cannot archive."

fi

# Logging
log_file="organizer.log"

# Log only happens when the archival was successful.
if [ -f "$new_file" ]; then
    echo "$timestamp : Archived '$original_file' as '$new_file'" >> "$log_file"
    echo "Archiving details logged in '$log_file'."
fi