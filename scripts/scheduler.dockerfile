# docker commands:
# docker build . --tag mushkevych/scheduler:2.0 --file scripts/scheduler.dockerfile
# docker run --network=schedulerdistrogit_syn-network --detach --name syn-scheduler --publish 5000:5000 mushkevych/scheduler:2.0
# docker -D run --name synergy-scheduler --network=schedulerdistrogit_syn-network --publish 5000:5000 -it mushkevych/scheduler:2.0 /bin/bash

# synergy-base is build from base.dockerfile
FROM mushkevych/synergy-base:0.2

LABEL maintainer="mushkevych@gmail.com"
LABEL synergy_scheduler.docker.version="0.2"

# set BoxID to *scheduler* and start Synergy Scheduler daemon
ENTRYPOINT ["/opt/synergy-distro/scripts/entrypoint.sh"]
CMD ["scheduler", "Scheduler"]

# port number the container should expose
EXPOSE 5000
