#!/bin/sh
#
# https://www.papertrail.com/solution/tips/how-to-live-tail-docker-logs/
#
docker logs --follow --tail 250 anchor-mongo-express
