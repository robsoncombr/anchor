#!/bin/sh
#
# https://hub.docker.com/_/mongo-express
#
docker container stop anchor-mongo-express
docker container rm anchor-mongo-express
docker run \
        --network convet \
        --name anchor-mongo-express \
        -p 8081:8081 \
        -e ME_CONFIG_MONGODB_ENABLE_ADMIN=true \
        -e ME_CONFIG_MONGODB_URL='mongodb://anchor-mongo5-dev:27017' \
        --restart always \
        -d mongo-express:latest
