# coding=utf-8
import os
import sys
import time
import random

from appium.webdriver.common.touch_action import TouchAction

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from baseView.baseView import BaseView, MobileBy


class DestinationPage(BaseView):

    where_to_go_button = (MobileBy.ACCESSIBILITY_ID, '您要去哪？')
    result_cell = (MobileBy.IOS_PREDICATE, "name=='Destination Index'")

    general_icon_drawer = (MobileBy.ACCESSIBILITY_ID, 'GeneralIconDrawer')

    def click_search_box(self):
        self.click(self.where_to_go_button)

    def click_destination_by_name(self, name):
        locator = (MobileBy.ACCESSIBILITY_ID, '%s' % name)
        self.click(locator)
        time.sleep(2)

    def select_result_by_name(self):
        draw = self.find_element(self.general_icon_drawer)

        draw_rect = draw.rect
        start_x = draw_rect['x']
        start_y = draw_rect['y']

        height, width = self.get_window_size()
        end_y = height * 1/4

        self.driver.execute_script("mobile:dragFromToForDuration",
                              {"duration": 0.5, "element": None, "fromX": start_x, "fromY": start_y, "toX": start_x, "toY": end_y})

        results = self.find_elements(self.result_cell)
        i = random.choice(range(len(results)))

        while True:
            results = self.find_elements(self.result_cell)
            visible = results[10].get_attribute('visible')

            if visible == 'true':
                results[10].click()
                break
            else:
                self.drag_up()



