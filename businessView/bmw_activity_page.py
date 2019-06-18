# coding=utf-8

from baseView.baseView import BaseView, MobileBy


class ActivityPage(BaseView):
    toggle_trip_button = (MobileBy.ACCESSIBILITY_ID, 'Toggle Trip Button')
    connect_to_usb_prompt = (MobileBy.ACCESSIBILITY_ID, '连接车辆，开始导航。')

    def click_toggle_trip_button(self):
        self.click(self.toggle_trip_button)

    # def get_usb_promopt_info(self):
    #     return self.find_element(ActivityPage)
