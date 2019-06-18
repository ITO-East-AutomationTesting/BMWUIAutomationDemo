# coding=utf-8
from baseView.baseView import BaseView, MobileBy


class ServicePage(BaseView):

    oil_card_tile = (MobileBy.ACCESSIBILITY_ID, '加油卡代充值')

    def select_tile(self, name):
        locator = (MobileBy.ACCESSIBILITY_ID, '%s' % name)
        tile = self.find_element(locator)
        while True:
            if tile is None:
                self.drag_up()
                tile = self.find_element(locator)
        self.click(locator)



