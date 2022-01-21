#!/bin/bash

set -euo pipefail

find apps/ -name pyproject.toml -exec dirname {} \; |
  while IFS="" read -r directory
    do
			echo "Updating README.md for Python package '$(basename "$directory")'..."
			cd "$directory" ||
			{
				echo -en "\r⚠️  Could not enter $directory"
				exit 1
			}
			poetry install
			make README.md -B
			cd - ||
			{
				echo -en "\r⚠️  Could not return to previous directory"
				exit 1
			}
			echo
    done
