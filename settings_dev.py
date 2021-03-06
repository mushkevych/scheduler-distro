from datetime import datetime
from os import environ

if 'SYN_START_TIMEPERIOD' in environ and environ['SYN_START_TIMEPERIOD']:
    SYN_START_TIMEPERIOD = environ['SYN_START_TIMEPERIOD']
else:
    SYN_START_TIMEPERIOD = datetime.utcnow().strftime('%Y%m%d%H')
# SYN_START_TIMEPERIOD = '2015032000',    # precision is process dependent

settings = dict(
    process_cwd='/tmp',   # daemonized process working directory, where it can create .cache and other folders

    mq_host='syn-rabbitmq',
    mq_user_id='guest',
    mq_password='guest',
    mq_vhost='/',
    mq_port=5672,
    mq_timeout_sec=None,

    mongodb_host_list=['mongodb://syn-mongodb:27017'],

    perf_ticker_interval=30,                        # seconds between performance tracker ticks
    synergy_start_timeperiod=SYN_START_TIMEPERIOD,  # precision is process dependent
    debug=True
)
