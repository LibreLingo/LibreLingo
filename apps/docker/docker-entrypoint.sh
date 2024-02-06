#!/bin/bash
set -euo pipefail
if [[ "${GIT_REPO}" == "TRUE" ]]; then
    if [ "$(ls -A /LibreLingo)" ]; then
       cd /LibreLingo
       git pull
     else
       cd /
       git clone https://github.com/LibreLingo/LibreLingo.git --single-branch
    fi
fi
cd /LibreLingo
yarn set version classic
yarn install --frozen-lockfile
poetry install
cd /LibreLingo/apps/librelingo_yaml_loader
poetry install
cd /LibreLingo/apps/librelingo_json_export
poetry install
yarn exportAllCourses # Exports all courses in /LibreLingo/courses
yarn web dev # Runs LibreLingo
