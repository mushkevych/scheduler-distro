#!/bin/bash

RABBITMQ_HOST=syn-rabbitmq

# simply wait for rabbit mq to come online
attempts=0
until wget http://${RABBITMQ_HOST}:15672/cli/rabbitmqadmin -O /tmp/rabbitmqadmin || [ ${attempts} -eq 5 ]; do
   sleep 10
   attempts=$((attempts + 1))
done

PROC_NAME=${1:-Scheduler}
/usr/bin/python /opt/synergy_scheduler/launch.py start --console ${PROC_NAME}
