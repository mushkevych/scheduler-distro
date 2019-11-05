#!/usr/bin/env bash

set -e

usage()
{
  cat <<@

  TMUX wrapper for docker-compose up

  Usage: $0 <SYN_ENVIRONMENT>

  How-to:
  - attach: tmux attach -t distro
  - stop: ctrl+c
  - detach: ctrl+b d
  - list sessions: tmux ls
@
  exit 1
}

if [[ $# -lt 1 ]]; then
  usage
fi

TARGET_ENV=${1:-"dev"}

echo "Starting Scheduler Distro..."

ROOT_PATH="$(dirname $(readlink -e $0))/.."
cd ${ROOT_PATH}
tmux new -d -s distro " export SYN_ENVIRONMENT=${TARGET_ENV}; docker-compose up | tee ${ROOT_PATH}/distro.out"
