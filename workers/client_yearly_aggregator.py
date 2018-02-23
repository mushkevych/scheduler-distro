__author__ = 'Bohdan Mushkevych'

from workers.client_monthly_aggregator import ClientMonthlyAggregator
from synergy.system import time_helper


class ClientYearlyAggregator(ClientMonthlyAggregator):
    """ illustration suite worker:
        - an aggregator from the client_monthly into the client_yearly """

    def __init__(self, process_name):
        super(ClientYearlyAggregator, self).__init__(process_name)

    def _init_sink_key(self, *args):
        return args[0], time_helper.month_to_year(args[1])


if __name__ == '__main__':
    from constants import PROCESS_CLIENT_YEARLY

    source = ClientYearlyAggregator(PROCESS_CLIENT_YEARLY)
    source.start()
