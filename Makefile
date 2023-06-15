help:
	@echo "dev-env                  create the dev environnement"
	@echo "build                    build stack"
	@echo "build-no-cache           build stack with --no-cache flag"
	@echo "up                       up stack"
	@echo "up-detach                up stack with --detach flag"
	@echo "up-dev                   up stack in dev mode"
	@echo "down                     down stack"
	@echo "pre-commit               make all checks to do before commit"
	@echo "tests                    make pytest"


compose := docker-compose -f compose.yml

dev-env:
	./scripts/setup_dev_env.sh

build:
	@$(compose) build

build-dev:
	@$(compose) -f compose-dev.yml build

build-no-cache:
	@$(compose) build --no-cache

up:
	@$(compose) up

up-detach:
	@$(compose) up --detach

up-dev:
	@$(compose) -f compose-dev.yml up

down:
	@$(compose) down

pre-commit:
	pre-commit run --all-file

tests:
	pytest


# Makefile text parsing special characters
NULL :=
SPACE := $(NULL) $(NULL)
COMMA := $(NULL),$(NULL)
