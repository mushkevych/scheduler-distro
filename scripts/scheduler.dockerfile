# docker commands:
# docker build . --tag mushkevych/scheduler:2.0
# docker run --network=schedulerdistrogit_syn-network --detach --name syn-scheduler --publish 5000:5000 mushkevych/scheduler:2.0
# docker -D run --name synergy-scheduler --network=schedulerdistrogit_syn-network -p 5000:5000 -it mushkevych/scheduler:2.0 /bin/bash

# synergy-base is build from base.dockerfile
FROM synergy-base:0.1

LABEL maintainer="mushkevych@gmail.com"
LABEL synergy_scheduler.docker.version="0.1"

# set BoxID to *scheduler* and start Synergy Scheduler daemon
ENTRYPOINT ["/opt/synergy-distro/scripts/entrypoint.sh"]
CMD ["scheduler", "Scheduler"]

# port number the container should expose
EXPOSE 5000
