#!/bin/sh
docker container stop anchor-learning
docker container rm anchor-learning
docker image rm anchor-learning
docker image build --file /nuvial/anchor/learning/docker/Dockerfile --tag anchor-learning .
