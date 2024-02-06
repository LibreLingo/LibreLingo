FROM ubuntu:jammy

# Setup to allow installing nvm
RUN mkdir /usr/local/nvm
ENV NVM_DIR /usr/local/nvm

# Setup to allow using poetry
ENV PATH="/root/.local/bin:$PATH"

# Make sure you have the latest version of things
RUN apt update

# Install basic dependencies
RUN apt-get install -y \
  curl \
  git \
  python-is-python3 \
  python3-venv \
  libpython3-dev \
  wget \
  unzip \
  gcc \
  libyaml-dev \
  npm

# replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# shell setup to be able to use nvm
SHELL ["/bin/bash", "--login", "-i", "-c"]

# Installing Node
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash

# shell setup to be able to use nvm
SHELL ["/bin/bash", "--login", "-c"]

# Install yarn
RUN npm install -g yarn

# Add project files
RUN git clone https://github.com/LibreLingo/LibreLingo.git  --single-branch

WORKDIR /LibreLingo

# Install node dependencies
RUN source $NVM_DIR/nvm.sh && nvm install 16 && nvm use 16 && yarn install

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python -

# Install Python dependencies
RUN poetry install
RUN cd apps/librelingo_yaml_loader && poetry install && cd ../.. && cd apps/librelingo_json_export && poetry install && cd ../..

# Prepare courses
RUN yarn web run installAllExternalCourses
RUN yarn exportAllCourses
