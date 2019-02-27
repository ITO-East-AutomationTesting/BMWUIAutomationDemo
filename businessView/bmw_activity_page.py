# coding=utf-8
import os
import sys
import time
import random

import self as self
from appium.webdriver.common.touch_action import TouchAction

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from baseView.baseView import BaseView, MobileBy


class ActivityPage(BaseView):
    toggle_trip_button = (MobileBy.ACCESSIBILITY_ID, 'Toggle Trip Button')
    connect_to_usb_prompt = (MobileBy.ACCESSIBILITY_ID, 'Connect to USB Prompt')

    def click_toggle_trip_button(self):
        self.click(self.toggle_trip_button)

    # def get_usb_promopt_info(self):
    #     return self.find_element(ActivityPage)
