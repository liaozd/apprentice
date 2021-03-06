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


# TECHNIQUE 27 Inspecting containers
docker ps -aq | xargs docker inspect --format='{{.NetworkSettings.IPAddress}}' | xargs -l1 ping -c1

# Forcing a rebuild without using the cache
docker build --no-cache .

# List the error exited containers
comm -3 \
<(docker ps -a -q --filter=status=exited | sort) \
<(docker ps -a -q --filter=exited=0 | sort) | \
xargs --no-run-if-empty docker inspect > error_containers

# TECHNIQUE 35 Housekeeping volumes
# https://github.com/docker-in-practice/docker-cleanup-volumes
docker run \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /var/lib/docker:/var/lib/docker \
--privileged dockerinpractice/docker-cleanup-volumes

# TECHNIQUE 38 Generate a dependency graph of your Docker images
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock   centurylink/image-graph > docker_images.png
