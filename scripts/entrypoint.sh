#!/bin/bash

RABBITMQ_HOST=syn-rabbitmq

# wait for rabbit mq to come online
attempts=0
until wget http://${RABBITMQ_HOST}:15672/cli/rabbitmqadmin -O /tmp/rabbitmqadmin || [ ${attempts} -eq 5 ]; do
   sleep 10
   attempts=$((attempts + 1))
done

SYN_BOX_ID=${1:-dev}
PROC_NAME=${2:-Scheduler}

/usr/bin/python /opt/synergy-distro/launch.py super --boxid ${SYN_BOX_ID}
/usr/bin/python /opt/synergy-distro/launch.py start --console ${PROC_NAME}
