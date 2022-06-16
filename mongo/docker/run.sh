#!/bin/sh
#
# https://hub.docker.com/_/mongo
#
docker container stop anchor-mongo5-dev
docker container rm anchor-mongo5-dev
docker run \
        --network convet \
        --name anchor-mongo5-dev \
        -v /nuvial/anchor/mongo/data:/data/db \
        -v /nuvial/anchor/mongo/dump:/dump \
        -e wiredTigerCacheSizeGB=1.5 \
        --restart always \
        -d mongo:latest mongod