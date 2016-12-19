#!/usr/bin/env bash

# Start a test docker server
docker run -d -p 2222:22 -ti ubuntu-ssh-server

# use hosts file
ansible docker-server -i hosts -m command -a uptime

# use ansible.cfg file
ansible docker-server -m ping

# install nginx
ansible docker-server -s -m apt -a "name=nginx update_cache=yes"