#!/usr/bin/env bash

# use hosts file
ansible testserver -i hosts -m command -a uptime

# use ansible.cfg file
ansible testserver -m ping
