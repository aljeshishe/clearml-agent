#!/bin/bash

set -ex

DOCKER_DIR=$(dirname "$0")
QUEUE_NAME=$1
cp ${DOCKER_DIR}/id_rsa_clearml_worker ~/.ssh/id_rsa_clearml_worker
clearml-agent --debug --config-file clearml.conf daemon --foreground --docker aljeshishe/agent-image:v1 --queue _grachev --create-queue --force-current-version --dynamic-gpus --queue _2gpu=2 _1gpu=1 
# clearml-agent --config-file clearml.conf daemon --docker aljeshishe/agent-image:v1 --queue ${QUEUE_NAME} --create-queue --detached --force-current-version
