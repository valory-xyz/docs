#!/bin/bash
set -e

while read -r line; do
    if [[ $line == *"path"* ]]; then
        submodule_path=$(echo $line | awk '{print $3}')
        cd $submodule_path
		echo "Updating $submodule_path"
        git pull origin main || exit 1 
        git checkout $(git tag | tail -n 1)
        cd ..
    fi
done < .gitmodules
