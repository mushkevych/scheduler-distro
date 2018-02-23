__author__ = 'Bohdan Mushkevych'

from constants import COLLECTION_SITE_DAILY
from tests import base_fixtures
from synergy.system.time_qualifier import QUALIFIER_DAILY

# pylint: disable=C0301
EXPECTED_SITE_DAILY_00 = {'stat': {'number_of_visits': 10055485624, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 9961459467, 'os': {'os_2': 195, 'os_0': 195, 'os_4': 195, 'os_1': 195, 'os_3': 195}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 195, 'browser_0': 195, 'browser_3': 195, 'browser_1': 195, 'browser_4': 195}}, 'domain': 'domain_name_32', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_01 = {'stat': {'number_of_visits': 3706279596, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 3942212607, 'os': {'os_2': 126, 'os_0': 126, 'os_4': 126, 'os_1': 126, 'os_3': 126}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 126, 'browser_0': 126, 'browser_3': 126, 'browser_1': 126, 'browser_4': 126}}, 'domain': 'domain_name_9', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_02 = {'stat': {'number_of_visits': 8069059883, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 8125995881, 'os': {'os_2': 144, 'os_0': 144, 'os_4': 144, 'os_1': 144, 'os_3': 144}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 144, 'browser_0': 144, 'browser_3': 144, 'browser_1': 144, 'browser_4': 144}}, 'domain': 'domain_name_15', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_03 = {'stat': {'number_of_visits': 10389755792, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 9201034556, 'os': {'os_2': 174, 'os_0': 174, 'os_4': 174, 'os_1': 174, 'os_3': 174}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 174, 'browser_0': 174, 'browser_3': 174, 'browser_1': 174, 'browser_4': 174}}, 'domain': 'domain_name_25', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_04 = {'stat': {'number_of_visits': 5247721597, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 7060629692, 'os': {'os_2': 117, 'os_0': 117, 'os_4': 117, 'os_1': 117, 'os_3': 117}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 117, 'browser_0': 117, 'browser_3': 117, 'browser_1': 117, 'browser_4': 117}}, 'domain': 'domain_name_6', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_05 = {'stat': {'number_of_visits': 6781536314, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 7512002913, 'os': {'os_2': 138, 'os_0': 138, 'os_4': 138, 'os_1': 138, 'os_3': 138}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 138, 'browser_0': 138, 'browser_3': 138, 'browser_1': 138, 'browser_4': 138}}, 'domain': 'domain_name_13', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_06 = {'stat': {'number_of_visits': 6782712095, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 3832674988, 'os': {'os_2': 147, 'os_0': 147, 'os_4': 147, 'os_1': 147, 'os_3': 147}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 147, 'browser_0': 147, 'browser_3': 147, 'browser_1': 147, 'browser_4': 147}}, 'domain': 'domain_name_16', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_07 = {'stat': {'number_of_visits': 6478001233, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 11295107631, 'os': {'os_2': 183, 'os_0': 183, 'os_4': 183, 'os_1': 183, 'os_3': 183}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 183, 'browser_0': 183, 'browser_3': 183, 'browser_1': 183, 'browser_4': 183}}, 'domain': 'domain_name_28', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_08 = {'stat': {'number_of_visits': 8489853188, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 9236514924, 'os': {'os_2': 189, 'os_0': 189, 'os_4': 189, 'os_1': 189, 'os_3': 189}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 189, 'browser_0': 189, 'browser_3': 189, 'browser_1': 189, 'browser_4': 189}}, 'domain': 'domain_name_30', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_09 = {'stat': {'number_of_visits': 4771161667, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 6237795001, 'os': {'os_2': 192, 'os_0': 192, 'os_4': 192, 'os_1': 192, 'os_3': 192}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 192, 'browser_0': 192, 'browser_3': 192, 'browser_1': 192, 'browser_4': 192}}, 'domain': 'domain_name_31', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_10 = {'stat': {'number_of_visits': 9477871275, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 9071356086, 'os': {'os_2': 141, 'os_0': 141, 'os_4': 141, 'os_1': 141, 'os_3': 141}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 141, 'browser_0': 141, 'browser_3': 141, 'browser_1': 141, 'browser_4': 141}}, 'domain': 'domain_name_14', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_11 = {'stat': {'number_of_visits': 8887688525, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 5860342344, 'os': {'os_2': 120, 'os_0': 120, 'os_4': 120, 'os_1': 120, 'os_3': 120}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 120, 'browser_0': 120, 'browser_3': 120, 'browser_1': 120, 'browser_4': 120}}, 'domain': 'domain_name_7', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_12 = {'stat': {'number_of_visits': 7507946895, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 10095159960, 'os': {'os_2': 132, 'os_0': 132, 'os_4': 132, 'os_1': 132, 'os_3': 132}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 132, 'browser_0': 132, 'browser_3': 132, 'browser_1': 132, 'browser_4': 132}}, 'domain': 'domain_name_11', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_13 = {'stat': {'number_of_visits': 5696835069, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 6780389787, 'os': {'os_2': 111, 'os_0': 111, 'os_4': 111, 'os_1': 111, 'os_3': 111}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 111, 'browser_0': 111, 'browser_3': 111, 'browser_1': 111, 'browser_4': 111}}, 'domain': 'domain_name_4', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_14 = {'stat': {'number_of_visits': 5508814077, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 7847034996, 'os': {'os_2': 114, 'os_0': 114, 'os_4': 114, 'os_1': 114, 'os_3': 114}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 114, 'browser_0': 114, 'browser_3': 114, 'browser_1': 114, 'browser_4': 114}}, 'domain': 'domain_name_5', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_15 = {'stat': {'number_of_visits': 5893860543, 'language': {'ua_uk': 28, 'ca_fr': 20, 'ca_en': 12, 'us_en': 36}, 'total_duration': 8583601154, 'os': {'os_2': 202, 'os_0': 202, 'os_4': 202, 'os_1': 202, 'os_3': 202}, 'screen_resolution': {'(320, 240)': 12, '(1280, 768)': 36, '(1024, 960)': 28, '(640, 480)': 20}, 'number_of_pageviews': 0, 'country': {'us': 36, 'fr': 20, 'uk': 28, 'ca': 12}, 'browser': {'browser_2': 202, 'browser_0': 202, 'browser_3': 202, 'browser_1': 202, 'browser_4': 202}}, 'domain': 'domain_name_1', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_16 = {'stat': {'number_of_visits': 4739343877, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 5027389517, 'os': {'os_2': 135, 'os_0': 135, 'os_4': 135, 'os_1': 135, 'os_3': 135}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 135, 'browser_0': 135, 'browser_3': 135, 'browser_1': 135, 'browser_4': 135}}, 'domain': 'domain_name_12', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_17 = {'stat': {'number_of_visits': 7076574466, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 6593569110, 'os': {'os_2': 180, 'os_0': 180, 'os_4': 180, 'os_1': 180, 'os_3': 180}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 180, 'browser_0': 180, 'browser_3': 180, 'browser_1': 180, 'browser_4': 180}}, 'domain': 'domain_name_27', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_18 = {'stat': {'number_of_visits': 7278963918, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 10544834320, 'os': {'os_2': 186, 'os_0': 186, 'os_4': 186, 'os_1': 186, 'os_3': 186}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 186, 'browser_0': 186, 'browser_3': 186, 'browser_1': 186, 'browser_4': 186}}, 'domain': 'domain_name_29', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_19 = {'stat': {'number_of_visits': 6132505375, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 4757308705, 'os': {'os_2': 129, 'os_0': 129, 'os_4': 129, 'os_1': 129, 'os_3': 129}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 129, 'browser_0': 129, 'browser_3': 129, 'browser_1': 129, 'browser_4': 129}}, 'domain': 'domain_name_10', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_20 = {'stat': {'number_of_visits': 9016224935, 'language': {'ua_uk': 28, 'ca_fr': 20, 'ca_en': 12, 'us_en': 36}, 'total_duration': 5875816061, 'os': {'os_2': 198, 'os_0': 198, 'os_4': 198, 'os_1': 198, 'os_3': 198}, 'screen_resolution': {'(320, 240)': 12, '(1280, 768)': 36, '(1024, 960)': 28, '(640, 480)': 20}, 'number_of_pageviews': 0, 'country': {'us': 36, 'fr': 20, 'uk': 28, 'ca': 12}, 'browser': {'browser_2': 198, 'browser_0': 198, 'browser_3': 198, 'browser_1': 198, 'browser_4': 198}}, 'domain': 'domain_name_0', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_21 = {'stat': {'number_of_visits': 6969334538, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 4188595032, 'os': {'os_2': 165, 'os_0': 165, 'os_4': 165, 'os_1': 165, 'os_3': 165}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 165, 'browser_0': 165, 'browser_3': 165, 'browser_1': 165, 'browser_4': 165}}, 'domain': 'domain_name_22', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_22 = {'stat': {'number_of_visits': 5570591226, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 6411667135, 'os': {'os_2': 156, 'os_0': 156, 'os_4': 156, 'os_1': 156, 'os_3': 156}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 156, 'browser_0': 156, 'browser_3': 156, 'browser_1': 156, 'browser_4': 156}}, 'domain': 'domain_name_19', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_23 = {'stat': {'number_of_visits': 9785568187, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 7652467740, 'os': {'os_2': 177, 'os_0': 177, 'os_4': 177, 'os_1': 177, 'os_3': 177}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 177, 'browser_0': 177, 'browser_3': 177, 'browser_1': 177, 'browser_4': 177}}, 'domain': 'domain_name_26', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_24 = {'stat': {'number_of_visits': 4386256557, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 7495103878, 'os': {'os_2': 108, 'os_0': 108, 'os_4': 108, 'os_1': 108, 'os_3': 108}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 108, 'browser_0': 108, 'browser_3': 108, 'browser_1': 108, 'browser_4': 108}}, 'domain': 'domain_name_3', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_25 = {'stat': {'number_of_visits': 8319126384, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 4583602128, 'os': {'os_2': 159, 'os_0': 159, 'os_4': 159, 'os_1': 159, 'os_3': 159}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 159, 'browser_0': 159, 'browser_3': 159, 'browser_1': 159, 'browser_4': 159}}, 'domain': 'domain_name_20', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_26 = {'stat': {'number_of_visits': 8240786643, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 3357027380, 'os': {'os_2': 123, 'os_0': 123, 'os_4': 123, 'os_1': 123, 'os_3': 123}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 123, 'browser_0': 123, 'browser_3': 123, 'browser_1': 123, 'browser_4': 123}}, 'domain': 'domain_name_8', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_27 = {'stat': {'number_of_visits': 3617998798, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 5087744634, 'os': {'os_2': 168, 'os_0': 168, 'os_4': 168, 'os_1': 168, 'os_3': 168}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 168, 'browser_0': 168, 'browser_3': 168, 'browser_1': 168, 'browser_4': 168}}, 'domain': 'domain_name_23', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_28 = {'stat': {'number_of_visits': 7259839655, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 8939107438, 'os': {'os_2': 162, 'os_0': 162, 'os_4': 162, 'os_1': 162, 'os_3': 162}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 162, 'browser_0': 162, 'browser_3': 162, 'browser_1': 162, 'browser_4': 162}}, 'domain': 'domain_name_21', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_29 = {'stat': {'number_of_visits': 6744558735, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 9031522402, 'os': {'os_2': 150, 'os_0': 150, 'os_4': 150, 'os_1': 150, 'os_3': 150}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 150, 'browser_0': 150, 'browser_3': 150, 'browser_1': 150, 'browser_4': 150}}, 'domain': 'domain_name_17', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_30 = {'stat': {'number_of_visits': 2414666973, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 5553888215, 'os': {'os_2': 171, 'os_0': 171, 'os_4': 171, 'os_1': 171, 'os_3': 171}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 171, 'browser_0': 171, 'browser_3': 171, 'browser_1': 171, 'browser_4': 171}}, 'domain': 'domain_name_24', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_31 = {'stat': {'number_of_visits': 8712860470, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 7332811545, 'os': {'os_2': 153, 'os_0': 153, 'os_4': 153, 'os_1': 153, 'os_3': 153}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 153, 'browser_0': 153, 'browser_3': 153, 'browser_1': 153, 'browser_4': 153}}, 'domain': 'domain_name_18', 'timeperiod': '2001030300'}
EXPECTED_SITE_DAILY_32 = {'stat': {'number_of_visits': 1687737504, 'language': {'ua_uk': 21, 'ca_fr': 15, 'ca_en': 9, 'us_en': 27}, 'total_duration': 6699097627, 'os': {'os_2': 105, 'os_0': 105, 'os_4': 105, 'os_1': 105, 'os_3': 105}, 'screen_resolution': {'(320, 240)': 9, '(1280, 768)': 27, '(1024, 960)': 21, '(640, 480)': 15}, 'number_of_pageviews': 0, 'country': {'us': 27, 'fr': 15, 'uk': 21, 'ca': 9}, 'browser': {'browser_2': 105, 'browser_0': 105, 'browser_3': 105, 'browser_1': 105, 'browser_4': 105}}, 'domain': 'domain_name_2', 'timeperiod': '2001030300'}
# pylint: enable=C0301


def generated_site_entries():
    return base_fixtures.create_site_stats(COLLECTION_SITE_DAILY, QUALIFIER_DAILY)


def clean_site_entries():
    return base_fixtures.clean_site_entries(COLLECTION_SITE_DAILY, QUALIFIER_DAILY)


if __name__ == '__main__':
    pass
