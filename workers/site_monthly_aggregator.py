__author__ = 'Bohdan Mushkevych'

from workers.site_daily_aggregator import SiteDailyAggregator
from synergy.system import time_helper


class SiteMonthlyAggregator(SiteDailyAggregator):
    """ illustration suite worker:
        - an aggregator from the site_daily into the site_monthly """

    def __init__(self, process_name):
        super(SiteMonthlyAggregator, self).__init__(process_name)

    def _init_sink_key(self, *args):
        return args[0], time_helper.day_to_month(args[1])


if __name__ == '__main__':
    from constants import PROCESS_SITE_MONTHLY

    source = SiteMonthlyAggregator(PROCESS_SITE_MONTHLY)
    source.start()
