# docker commands:
# docker build . --tag mushkevych/worker:2.0
# docker run --network=schedulerdistrogit_syn-network --detach --name syn-worker --publish 5000:5000 mushkevych/worker:2.0
# docker -D run --name synergy-worker --network=schedulerdistrogit_syn-network -p 5000:5000 -it mushkevych/worker:2.0 /bin/bash

# synergy-base is build from base.dockerfile
FROM synergy-base:0.1

LABEL maintainer="mushkevych@gmail.com"
LABEL synergy_worker.docker.version="0.1"

# set BoxID to *dev* and start Supervisor daemon
ENTRYPOINT ["/opt/synergy-distro/scripts/entrypoint.sh"]
CMD ["dev", "Supervisor"]

# port number the container should expose
EXPOSE 5000
