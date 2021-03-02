#!/bin/bash

./scripts/updatePypiReadmeFiles.sh -B

if git diff-index --quiet HEAD --; then
	echo "🎉 Amazing, PyPi readme files are up to date"
else
	echo "😿 Outdated PyPi readme files detected."
	echo "The following files were outdated:"
	git status
	echo "Run the following script to automatically update the readme files:"
	echo "./scripts/updatePypiReadmeFiles.sh"
	exit 1
fi
