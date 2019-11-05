# docker commands:
# docker build . --tag mushkevych/worker:2.0 --file scripts/worker.dockerfile
# docker run --network=schedulerdistrogit_syn-network --detach --name syn-worker mushkevych/worker:2.0
# docker -D run --name synergy-workers --network=schedulerdistrogit_syn-network -it mushkevych/worker:2.0 /bin/bash
#
# connect to running container:
# docker exec -it synergy-workers /bin/bash

# synergy-base is build from base.dockerfile
FROM mushkevych/synergy-base:0.2

LABEL maintainer="mushkevych@gmail.com"
LABEL synergy_worker.docker.version="0.2"

# set BoxID to *dev* and start Supervisor daemon
ENTRYPOINT ["/opt/synergy-distro/scripts/entrypoint.sh"]
CMD ["dev", "Supervisor"]
