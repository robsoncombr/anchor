#!/bin/sh
docker container stop anchor-learning
docker container rm anchor-learning
docker run \
        --network convet \
        -p 5000:5000 \
        -v /nuvial/anchor/learning:/anchor \
        --restart always \
        -d -t --name anchor-learning anchor-learning
