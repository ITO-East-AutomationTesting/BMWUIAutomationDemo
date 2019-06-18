# coding=utf-8

from baseView.baseView import BaseView, MobileBy


class MorePage(BaseView):

    logout_button = (MobileBy.ACCESSIBILITY_ID, 'Logout Button')
    title_label = (MobileBy.ACCESSIBILITY_ID, 'Title Label')
    yes_button = (MobileBy.ACCESSIBILITY_ID, 'Yes Button')
    no_button = (MobileBy.ACCESSIBILITY_ID, 'No Button')

    def click_button_by_name(self, name):
        locator = (MobileBy.ACCESSIBILITY_ID, '%s' % name)
        self.click(locator)

    def get_title_label(self):
        return self.get_attribute(self.title_label, 'label')

    def is_logout_click(self, logout=True):
        if logout:
            self.click(self.yes_button)
        else:
            self.click(self.no_button)

    def click_logout_button(self):
        self.drag_up()
        self.click(self.logout_button)
