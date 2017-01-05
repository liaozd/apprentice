#!/usr/bin/env bash

# Build one test server
docker build -t ubuntu-ssh-server .

# Start a test docker server
docker run -d -p 2222:22 -p 8080:80 -p 8443:443 ubuntu-ssh-server
docker run -d -p 2223:22 -p 8081:80 -p 8444:443 ubuntu-ssh-server
docker run -d -p 2224:22 -p 8082:80 -p 8445:443 ubuntu-ssh-server

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

# Ansible automactically defines a group called `all` or `*` include all of the hosts in the inventory
ansible all -a "date"
ansible '*' -a "date"

# Capture command return
ansible-playbook whoami.yml
