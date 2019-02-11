# coding=utf-8
import os
import random
import string
import sys

from appium.webdriver.common.mobileby import MobileBy

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from baseView.baseView import BaseView, NoSuchElementException


class Common(BaseView):

    skip_button = (MobileBy.ACCESSIBILITY_ID, 'Skip Button')

    def skip_load_page(self):
        try:
            ele = self.driver.find_element(*self.skip_button)
        except NoSuchElementException:
            pass
        else:
            ele.click()

    @staticmethod
    def generate_user_name():
        username = ''.join(random.choice(string.ascii_letters) for i in range(5))
        return username

    @staticmethod
    def generate_phone_number():
        phone_number = '1' + ''.join(random.choice("0123456789") for i in range(10))
        return phone_number

    @staticmethod
    def generate_passport_number():
        passport = 'h' + ''.join(random.choice("0123456789") for i in range(17))
        return passport

    @staticmethod
    def generate_car_id_number():
        car_id = ''.join(random.choice("0123456789") for i in range(19))
        return car_id
