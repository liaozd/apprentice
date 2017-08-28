#!/usr/bin/env bash

# gitlab
sudo docker run --detach \
    --hostname gitlab.example.com \
    --publish 443:443 --publish 80:80 --publish 2222:22 \
    --name gitlab \
    --restart always \
    --volume /srv/gitlab/config:/etc/gitlab \
    --volume /srv/gitlab/logs:/var/log/gitlab \
    --volume /srv/gitlab/data:/var/opt/gitlab \
    gitlab/gitlab-ce:latest

# TECHNIQUE 21 Retain your container's bash history
docker run -e HISTFILE=/root/.bash_history -v $HOME/.bash_history:/root/.bash_history -ti ubuntu /bin/bash

# TECHNIQUE 25 Dev tools container
docker run -t -i \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY \
--net=host --ipc=host \
-v /opt/workspace:/home/dockerinpractice \
dockerinpractice/docker-dev-tools-image # ubuntu

## 1
# Firefox docker
FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y firefox

RUN groupadd -g 1000 neo
RUN useradd -d /home/neo -s /bin/bash -m neo -u 1000 -g 1000
USER neo
ENV home /home/neo
CMD /usr/bin/firefox

## 2
docker build -t gui .

## 3
docker run -v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY \
-h $HOSTNAME \
-v $HOME/.Xauthority:/home/$USER/.Xauthority \
gui
