#! /usr/bin/env sh

# Exit in case of error
set -e

docker stack deploy -c docker-stack.yml --with-registry-auth "${STACK_NAME?Variable not set}"
