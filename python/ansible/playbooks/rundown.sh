#!/usr/bin/env bash

# Build one test server
docker build -t ubuntu-ssh-server .

# Start a test docker server
docker run -d -p 2222:22 -p 8080:80 -p 8443:443 ubuntu-ssh-server

# ssh into the ubuntu-ssh-server
sshpass -p 'screencast' ssh -p 2222 root@localhost

# use hosts file
ansible docker-server -i hosts -m command -a uptime

# use ansible.cfg file
ansible docker-server -m ping

# install nginx
ansible docker-server -s -m apt -a "name=nginx update_cache=yes"

# host pi server
ansible pi-server -m ping

# Create TLS certificate
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -subj /CN=localhost -keyout files/nginx.key -out files/nginx.crt

# Start a tls
ansible-playbook web-tls.yml
