# coding=utf-8
import os
import sys
import unittest
import warnings
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from businessView.bwm_login_page import LoginPage
from businessView.bwm_main_page import MainPage
from businessView.bwm_more_page import MorePage
from businessView.bwm_destination_page import DestinationPage
from common.bwm_caps import bwm_desired
from common.common_fun import Common


class TestDemo(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = bwm_desired()
        self.commonView = Common(self.driver)
        self.commonView.skip_load_page()

    def tearDown(self):
        self.commonView.get_screenshot()
        self.driver.quit()

    def test_login_demo(self):
        u'''Test Login With Phone And Password'''
        print('1. 输入手机号码和密码.')
        loginPage = LoginPage(self.driver)
        loginPage.login_bwm('15606130210', '0210zhuxia')

        # print('2. 创建Pin码.')
        # self.assertEqual('创建4位数PIN码', loginPage.get_pin_message())
        # loginPage.create_pin_password(1, 2, 3, 4)
        #
        # print('3. 重新输入Pin码.')
        # self.assertEqual('请重新输入PIN码来验证', loginPage.get_pin_message())
        # loginPage.create_pin_password(1, 2, 3, 4)
        #
        # print('4. 是否启用Touch ID.')
        # loginPage.is_enable_touch_id()

    def test_choose_destination(self):
        u'''Test Go To A Destination'''
        print('1. 输入Pin码.')
        loginPage = LoginPage(self.driver)
        loginPage.create_pin_password(1, 2, 3, 4)

        print('2. 点击目的地.')
        mainPage = MainPage(self.driver)
        mainPage.click_bottom_button_by_name('目的地')

        print('2. 点击想要去哪里.')
        destinationPage = DestinationPage(self.driver)
        destinationPage.click_search_box()

        print('3. 点击加油站.')
        destinationPage.click_destination_by_name('加油站')

        destinationPage.select_result_by_name()

    def test_login_out_demo(self):
        u'''Test Logout BWM APP.'''
        print('1. 输入Pin码.')
        loginPage = LoginPage(self.driver)
        loginPage.create_pin_password(1, 2, 3, 4)

        print('2. 点击更多.')
        mainPage = MainPage(self.driver)
        mainPage.click_bottom_button_by_name('更多')

        print('3. 点击个人资料.')
        morePage = MorePage(self.driver)
        morePage.click_button_by_name('个人资料')

        print('4. 点击注销.')
        morePage.click_logout_button()
        self.assertEqual('是否确定要注销？', morePage.get_title_label())

        print('5. 确定是否注销.')
        morePage.is_logout_click()


if __name__ == '__main__':
    unittest.main()
