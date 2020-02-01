#!/usr/bin/env bash

set -e

usage()
{
  cat <<@

  TMUX wrapper for docker-compose up

  Usage: $0 <SYN_ENVIRONMENT> <SYN_START_TIMEPERIOD>

  How-to:
  - attach: tmux attach -t distro
  - stop: ctrl+c
  - detach: ctrl+b d
  - list sessions: tmux ls
@
  exit 1
}

if [[ $# -lt 2 ]]; then
  usage
fi

TARGET_ENV=${1:-"dev"}
SYN_START_TIMEPERIOD=${2:-$(date -d "-1 days" +%Y%m%d%H)}  # by default - read yesterday's date in YYYYMMDDHH format
REGISTRY_URI=""

echo "Initializing filesystem..."
sudo mkdir -p /data/scheduler-distro/db
sudo mkdir -p /data/scheduler-distro/scheduler
sudo mkdir --mode=777 -p /data/scheduler-distro/scheduler/log
sudo mkdir -p /data/scheduler-distro/workers
sudo mkdir --mode=777 -p /data/scheduler-distro/workers/log
sudo mkdir -p /data/scheduler-distro/rabbitmq

echo "Starting Scheduler Distro..."

ROOT_PATH="$(dirname $(readlink -e $0))/.."
cd ${ROOT_PATH}

sudo cp ./settings_${TARGET_ENV}.py /data/scheduler-distro/scheduler/
sudo cp ./settings_${TARGET_ENV}.py /data/scheduler-distro/workers/

#export PRIVATE_REGISTRY_URI=${REGISTRY_URI}; export SYN_ENVIRONMENT=${TARGET_ENV}; docker-compose up
tmux new -d -s distro "export PRIVATE_REGISTRY_URI=${REGISTRY_URI}; export SYN_ENVIRONMENT=${TARGET_ENV}; export SYN_START_TIMEPERIOD=${SYN_START_TIMEPERIOD}; docker-compose up | tee ${ROOT_PATH}/distro.out"
