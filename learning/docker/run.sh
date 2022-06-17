#!/bin/sh
docker container stop anchor-learning
docker container rm anchor-learning
docker run \
        --network convet \
        -p 5000:5000 \
        -v /nuvial/anchor/learning/app/run.py:/anchor/run.py \
        -v /nuvial/anchor/learning/app/config.py:/anchor/config.py \
        -v /nuvial/anchor/learning/app:/anchor/app \
        --restart always \
        -d -t --name anchor-learning anchor-learning
