#!/bin/bash

# step 1: wait for rabbit mq to come online
RABBITMQ_HOST=syn-rabbitmq

attempts=0
until wget http://${RABBITMQ_HOST}:15672/cli/rabbitmqadmin -O /tmp/rabbitmqadmin || [[ ${attempts} -eq 5 ]]; do
   sleep 10
   attempts=$((attempts + 1))
done

# step 2: /opt/synergy-distro/configuration is mapped from the HOST with docker --volume mechanism
# --no-clobber prevents overwriting of existing files
touch /opt/synergy-distro/configuration/__init__.py
mv --no-clobber /opt/synergy-distro/settings_*.py /opt/synergy-distro/configuration/ || true
mv --no-clobber /opt/synergy-distro/flows_*.py /opt/synergy-distro/configuration/ || true
mv --no-clobber /opt/synergy-distro/context_*.py /opt/synergy-distro/configuration/ || true

# step 3: define a boxid and start the process
SYN_BOX_ID=${1:-scheduler}
PROC_NAME=${2:-Scheduler}
/usr/bin/python /opt/synergy-distro/launch.py super --boxid ${SYN_BOX_ID}

SCHEDULER_DB_MARKER="/opt/synergy-distro/configuration/scheduler_db.marker"
if [[ ${PROC_NAME} == "Scheduler" ]]; then
    if [[ ! -f ${SCHEDULER_DB_MARKER} ]]; then
        /usr/bin/python /opt/synergy-distro/launch.py db --reset
        /usr/bin/python /opt/synergy-distro/launch.py super --reset
        touch ${SCHEDULER_DB_MARKER}
    fi
    /usr/bin/python /opt/synergy-distro/launch.py db --update
fi

SUPERVISOR_DB_MARKER="/opt/synergy-distro/configuration/supervisor_db.${SYN_BOX_ID}.marker"
if [[ ${PROC_NAME} == "Supervisor" ]]; then
    sleep 10s   # wait for Scheduler to initialize DB
    /usr/bin/python /opt/synergy-distro/launch.py super --update
    touch ${SUPERVISOR_DB_MARKER}
fi
/usr/bin/python /opt/synergy-distro/launch.py start --console ${PROC_NAME}
