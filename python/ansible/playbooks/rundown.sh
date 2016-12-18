#!/usr/bin/env bash

# use hosts file
ansible piserver -i hosts -m command -a uptime

# use ansible.cfg file
ansible piserver -m ping

# install nginx
ansible piserver -s -m apt -a "name=nginx update_cache=yes"