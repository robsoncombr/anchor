#!/bin/sh
docker container stop anchor-learning
docker container rm anchor-learning
docker run \
        --network convet \
        -p 5000:80 \
        -v /nuvial/anchor/learning/app:/ve/app \
        --restart always \
        -d -t --name anchor-learning anchor-learning
