FROM debian:jessie
MAINTAINER Liao Zhuodi <liao_zd@hotmail.com>

RUN apt-get -y update
RUN apt-get -y install iptables \
                       net-tools \
                       vim

CMD ["/bin/bash"]