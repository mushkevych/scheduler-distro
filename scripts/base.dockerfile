# docker commands:
# docker system prune -a --volumes
# docker build . --tag mushkevych/synergy-base:0.2 --file scripts/base.dockerfile
# docker -D run --name synergy-base --network=schedulerdistrogit_syn-network -it mushkevych/synergy-base:0.2 /bin/bash

ARG private_registry_uri=

# list of alpine packages: https://pkgs.alpinelinux.org/packages
FROM ${private_registry_uri}alpine:3.10

LABEL maintainer="mushkevych@gmail.com"
LABEL synergy-base.docker.version="0.2"

# OS-level required packages:
#   * dumb-init: a proper init system for containers, to reap zombie children
#   * linux-headers: commonly needed, and an unusual package name from Alpine.
#   * build-base: include basic development packages (gcc, g++, etc)
#   * bash gawk sed grep bc coreutils: bash & shell utils
#   * ca-certificates: for SSL verification during Pip and easy_install
ENV PACKAGES="\
  dumb-init \
  linux-headers \
  build-base \
  bash gawk sed grep bc curl coreutils \
  ca-certificates \
"
RUN apk add --no-cache ${PACKAGES}

# add python3, python3-dev and pip
# NOTE: do not remove ensurepip module
RUN apk add --no-cache python3 python3-dev && \
    python3 -m ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [[ ! -e /usr/bin/pip ]]; then ln -s pip3 /usr/bin/pip; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

COPY . /opt/synergy-distro
WORKDIR /opt/synergy-distro/

RUN mkdir -p /var/log/synergy-distro/

RUN /opt/synergy-distro/launch.py install
