#!/bin/sh

docker container stop anchor-mongo5-dev
docker container start anchor-mongo5-dev

/nuvial/anchor/mongo/express/restart.sh
