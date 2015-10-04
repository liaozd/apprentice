#!/usr/bin/env bash

docker build -t iptables .

docker run --rm --privileged=true --name iptablestest -it iptables
# --privileged=true  enable iptables inside the container