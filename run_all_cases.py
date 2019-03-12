# coding=utf-8

import unittest
import HTMLTestRunnerCN
import time
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from BeautifulReport.BeautifulReport import BeautifulReport
from common import send_email


base_dir = os.path.dirname(os.path.realpath(__file__))
test_cases_path = os.path.join(base_dir, 'test_case')


def create_suite():
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_cases_path, pattern='test_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTest(test_case)
    return suite


now = time.strftime('%Y%m%d%H%M%S')
reportFile = "test_report_" + now + ".html"
reportFilePath = os.path.join(base_dir, 'reports', reportFile)

all_test_cases = create_suite()
result = BeautifulReport(all_test_cases)
result.report(filename="bwm_ui_automation_" + time.strftime('%Y%m%d%H%M%S') + ".html",
              description='BMW UI Automation Report',
              log_path=reportFilePath)

# time.sleep(10)
#
# email = send_email.SendEmail()
# email.sendReport()