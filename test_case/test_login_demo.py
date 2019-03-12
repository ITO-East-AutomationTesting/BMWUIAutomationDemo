# coding=utf-8
import os
import sys
import unittest
import warnings
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from businessView.bwm_login_page import LoginPage
from businessView.bwm_main_page import MainPage
from businessView.bwm_more_page import MorePage
from businessView.bwm_destination_page import DestinationPage
from businessView.bmw_activity_page import ActivityPage
from common.bwm_caps import bwm_desired
from common.common_fun import Common
from BeautifulReport.BeautifulReport import BeautifulReport
from multiprocessing.dummy import Pool as ThreadPool

base_dir = os.path.dirname(os.path.dirname(__file__))


def save_img(self, img_name):
    img_path = os.path.join(base_dir, 'img')
    if self.web_driver is not None:
        self.web_driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))
    else:
        self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))


class TestDemo(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = bwm_desired()
        self.commonView = Common(self.driver)
        self.commonView.skip_load_page()

    def tearDown(self):
        self.commonView.get_screenshot()
        self.driver.quit()

    #
    # def test_login_demo(self):
    #     u'''Test Login With Phone And Password'''
    #     print('1. 输入手机号码和密码.')
    #     loginPage = LoginPage(self.driver)
    #     loginPage.login_bwm('15606130210', '0210zhuxia')

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

    @BeautifulReport.add_test_img('test_choose_destination_{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_choose_destination(self):
        u'''Test Go To A Destination'''
        print('1. 输入Pin码.')
        loginPage = LoginPage(self.driver)
        # pool = ThreadPool(4)
        # pool.map(loginPage.input_pin_code, [1, 2, 3, 4])
        # pool.close()
        # pool.join()
        # map(loginPage.input_pin_code, [1, 2, 3, 4])

        for value in [1, 2, 3, 4]:
            loginPage.input_pin_code(value)
        # loginPage.input_pin_password(1, 2, 3, 4)


        print('2. 点击目的地.')
        mainPage = MainPage(self.driver)
        # mainPage.click_bottom_button_by_name('车辆')
        # self.assertEqual(mainPage.get_attribute())
        mainPage.click_bottom_button_by_name('目的地')

        print('2. 点击想要去哪里.')
        destinationPage = DestinationPage(self.driver)
        destinationPage.click_search_box()

        print('3. 点击加油站.')
        destinationPage.click_destination_by_name('加油站')

        print('4. 随机选择加油站')
        destinationPage.select_result_by_name()

        print('5. 出发')
        destinationPage.click_start_trip_button()

        print('6. 跳转到活动页面')
        mainPage.click_bottom_button_by_name('活动')

        print('7.关闭active活动行程')
        activityPage = ActivityPage(self.driver)

        self.assertEqual(activityPage.get_attribute(activityPage.connect_to_usb_prompt, 'value'), '连接车辆，开始导航。')
        activityPage.click_toggle_trip_button()

    # self.assertEquals()
    @BeautifulReport.add_test_img('test_login_out_demo_{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_login_out_demo(self):
        u'''Test Logout BWM APP.'''
        print('1. 输入Pin码.')
        loginPage = LoginPage(self.driver)

        for value in [1, 2, 3, 4]:
            loginPage.input_pin_code(value)

        print('2. 点击更多.')
        mainPage = MainPage(self.driver)
        mainPage.click_bottom_button_by_name('更多')

        # print('3. 点击个人资料.')
        # morePage = MorePage(self.driver)
        # morePage.click_button_by_name('个人资料')
        #
        # print('4. 点击注销.')
        # morePage.click_logout_button()
        # self.assertEqual('是否确定要注销？', morePage.get_title_label())
        #
        # print('5. 确定是否注销.')
        # morePage.is_logout_click()


if __name__ == '__main__':
    unittest.main()
