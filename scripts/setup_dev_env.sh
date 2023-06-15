#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

GREEN="\e[1;92m"
CYAN="\e[1;96m"
RESET="\e[0m"

ENV_NAME=project-api
PYTHON_VERSION=3.11.4
POETRY_VERSION=1.5.1

echo -e "${GREEN}Creating a virtualenv ${CYAN}${ENV_NAME}${GREEN} with Python ${CYAN}${PYTHON_VERSION}${RESET}"
rm -f .python-version
pyenv install ${PYTHON_VERSION} --skip-existing
pyenv virtualenv ${PYTHON_VERSION} ${ENV_NAME} --force
pyenv local ${ENV_NAME}

echo -e "${GREEN}Updating pip, setuptools & wheel${RESET}"
pip install --upgrade pip setuptools wheel

echo -e "${GREEN}Install poetry${RESET}"
pip install poetry==${POETRY_VERSION}

echo -e "${GREEN}Install dependencies with poetry${RESET}"
poetry config virtualenvs.create false
poetry install

echo -e "${GREEN}Install pre-commit dependencies${RESET}"
pre-commit install

echo -e "${GREEN}All set !${RESET}"
