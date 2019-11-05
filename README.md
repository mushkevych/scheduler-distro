Synergy Scheduler Distribution
=========

This repository serves as a distro for Synergy Scheduler, Synergy Flow, Synergy Workers.  
Project provides Docker containers for Synergy Scheduler and Synergy Workers; 
docker-compose for the complete env: Scheduler, Workers, MongoDB, RabbitMQ;


License:
---------
[BSD 3-Clause License.](http://en.wikipedia.org/wiki/BSD_licenses#3-clause_license_.28.22Revised_BSD_License.22.2C_.22New_BSD_License.22.2C_or_.22Modified_BSD_License.22.29)
Refer to LICENSE for details.


Wiki:
---------
[Installation, Setup, How-to](https://github.com/mushkevych/scheduler-distro/wiki)


Git repositories of included projects:
---------
[Synergy Scheduler GitHub page](https://github.com/mushkevych/scheduler)  
[Synergy Flow GitHub page](https://github.com/mushkevych/synergy_flow)  
[Distro GitHub project page](https://github.com/mushkevych/scheduler-distro)  


Metafile:
---------

    /docker-compose.yml   environment orchestration file
    /launch.py            launcher file
    /process_starter.py   utility to start a process in a daemon mode
    /constants.py         configuration management - constants
    /context.py           configuration management - registrar of all known processes
    /settings.py          configuration management - environment-specific settings
    /setup.py             Distutils setup script
    /configuration/       folder contains settings.xxx file which becomes visible to container
    /scripts/             folder contains Dockerfiles and shell helper scripts 
    /tests/               folder contains unit test
    /vendors/             folder contains Python libraries required by the project and installed in Python Virtual Environment
    /worker/              folder contains illustration suite workers (job runners)  
    /db/                  root folder for illustration suite database components - models, dao, schema


OS-Level Dependencies
---------
1. linux/unix  
1. python 3.7+
1. docker, docker-compose
