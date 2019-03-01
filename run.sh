#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
    if grep -q $line "success.txt"; then
        echo "Ignoring already succeessfull: $line"
    else
        echo "Checking $line..."
        python run.py $line
        code=$?

        if [ $code -ne 0 ]; then
            echo "FAILED"
        else
            echo "SUCCESS"
            echo $line >> success.txt
        fi
    fi

    echo ""
done < "$1"


