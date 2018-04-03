from datetime import datetime
from os import environ
ENVIRONMENT = environ.get('SYN_ENVIRONMENT', 'dev')

# folder locations, connection properties etc
settings = dict(
    process_prefix='Synergy',   # global prefix that is added to every process name started for synergy-scheduler
    process_cwd='/mnt/tmp',     # daemonized process working directory, where it can create .cache and other folders
    process_start_time=datetime.utcnow(),
    config_file='/etc/synergy.conf',
    version='%BUILD_NUMBER%',

    log_directory='/var/log/synergy-distro/',
    pid_directory='/var/log/synergy-distro/',

    bash_runnable_count=5,      # number of concurrently running shell scripts supported by BashDriver

    ds_type='mongo_db',
    mongo_db_name='scheduler',
    db_log_ttl_days=365,        # number of days to keep entries in the log_recordings collection/table
    batch_size=1024,            # illustration suite setting: number of DB documents to read in batch

    debug=False,                # if True, logger.setLevel is set to DEBUG. Otherwise to INFO

    under_test=False            # marks execution of the Unit Tests
                                # if True, a console handler for STDOUT and STDERR are appended to the logger.
                                # Otherwise STDOUT and STDERR are redirected to .log files
)

# Update current dict with the environment-specific settings
overrides = __import__('settings_{0}'.format(ENVIRONMENT), fromlist=['configuration'])
settings.update(overrides.settings)


# Modules to test and verify (pylint/pep8)
testable_modules = [
    'synergy',
    'db',
    'workers',
]

test_cases = [
    'tests.test_tree_node',
    'tests.test_multi_level_tree',
    'tests.test_process_hierarchy',
    'tests.test_abstract_state_machine',
    'tests.test_state_machine_recomputing',
    'tests.test_state_machine_continuous',
    'tests.test_state_machine_discrete',
    'tests.test_publishers_pool',
    'tests.test_garbage_collector',
    'tests.test_priority_queue',
    'tests.test_repeat_timer',
    'tests.test_event_clock',
    'tests.test_system_utils',
    'tests.test_time_helper',
    'tests.test_timeperiod_dict',
    'tests.test_process_starter',
    'tests.test_log_recording_handler',
    'tests.test_site_hourly_aggregator',
    'tests.test_site_daily_aggregator',
    'tests.test_site_monthly_aggregator',
    'tests.test_site_yearly_aggregator',
    'tests.test_raw_data',
    'tests.test_site_statistics',
    'tests.test_single_session',
    'tests.test_freerun_process_entry',
]


def enable_test_mode():
    if settings['under_test']:
        # test mode is already enabled
        return

    # mq_vhost is created with: sudo rabbitmqctl add_vhost unit_test
    # permissions are set with: sudo rabbitmqctl set_permissions -p unit_test guest ".*" ".*" ".*"
    test_settings = dict(
        mongo_db_name=settings['mongo_db_name'] + '_test',
        #mq_vhost='unit_test',
        debug=True,
        under_test=True,
        synergy_start_timeperiod=datetime.utcnow().strftime('%Y%m%d%H'),
    )
    settings.update(test_settings)

    # it is safe to import global settings at this point
    # since the environment-specific settings has been loaded above
    from synergy.conf import settings as global_settings
    global_settings.settings.update(test_settings)

    from tests.ut_context import register_processes
    register_processes()
