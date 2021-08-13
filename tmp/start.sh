#!/bin/bash

set -ex

DOCKER_DIR=$(dirname "$0")
QUEUE_NAME=$1
cp ${DOCKER_DIR}/id_rsa_clearml_worker ~/.ssh/id_rsa_clearml_worker
clearml-agent --config-file clearml.conf daemon --docker aljeshishe/agent-image:v1 --queue ${QUEUE_NAME} --create-queue --detached --force-current-version