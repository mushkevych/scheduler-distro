#!/bin/bash

# step 1: wait for rabbit mq to come online
RABBITMQ_HOST=syn-rabbitmq

attempts=0
until wget http://${RABBITMQ_HOST}:15672/cli/rabbitmqadmin -O /tmp/rabbitmqadmin || [[ ${attempts} -eq 5 ]]; do
   sleep 10
   attempts=$((attempts + 1))
done

# step 2: /opt/synergy-distro/configuration is mapped from the HOST with docker --volume mechanism
# copy settings_dev.py
touch /opt/synergy-distro/configuration/__init__.py
mv /opt/synergy-distro/settings_*.py /opt/synergy-distro/configuration/ || true
mv /opt/synergy-distro/flows_*.py /opt/synergy-distro/configuration/ || true
mv /opt/synergy-distro/context_*.py /opt/synergy-distro/configuration/ || true

# step 3: define a boxid and start the process
SYN_BOX_ID=${1:-dev}
PROC_NAME=${2:-Scheduler}

/usr/bin/python /opt/synergy-distro/launch.py super --boxid ${SYN_BOX_ID}
/usr/bin/python /opt/synergy-distro/launch.py start --console ${PROC_NAME}
