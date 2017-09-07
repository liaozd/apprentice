#!/usr/bin/env bash

docker build -t mysecret .
docker run -d mysecret /bin/true
# Flattening images
docker export 6cc2031f7d84  | docker import - mysecret
docker history mysecret
