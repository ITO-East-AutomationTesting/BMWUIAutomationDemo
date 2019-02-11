# coding=utf-8
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from baseView.baseView import BaseView, MobileBy


class MainPage(BaseView):
    more_button = (MobileBy.ACCESSIBILITY_ID, '更多')
    cars_button = (MobileBy.ACCESSIBILITY_ID, '车辆')
    destination_button = (MobileBy.ACCESSIBILITY_ID, '目的地')
    activity_button = (MobileBy.ACCESSIBILITY_ID, '活动')
    service_button = (MobileBy.ACCESSIBILITY_ID, '服务')

    def click_bottom_button_by_name(self, name):
        button = (MobileBy.ACCESSIBILITY_ID, '%s' % name)
        self.click(button)
