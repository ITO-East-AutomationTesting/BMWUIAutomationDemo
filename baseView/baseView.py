# coding=gbk
import logging
import os
import sys
import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class BaseView(object):
    # btn = (MobileBy.IOS_PREDICATE, 'label=="隐藏键盘"')
    btn = (MobileBy.ACCESSIBILITY_ID, 'Done')

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc):
        logging.info('Find element by %s: %s' % (loc[0], loc[1]))

        try:
            element = WebDriverWait(self.driver, 10).until(lambda x:x.find_element(*loc))
            return element
        except NoSuchElementException:
            logging.error('Can not find element: %s' % loc[1])
            raise
        except TimeoutException:
            logging.error('Time out to find element: %s' % loc[1])
            raise

    def find_elements(self, loc):
        logging.info('Find elements by %s: %s' % (loc[0], loc[1]))
        try:
            elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator=loc))
            return elements
        except NoSuchElementException:
            logging.error('Can not find element: %s' % loc[1])
            self.get_screenshot()
            raise

    def click(self, loc):
        try:
            ele = self.find_element(loc)
            logging.info('Click element by %s: %s' % (loc[0], loc[1]))
            ele.click()
            # time.sleep(1)
        except AttributeError:
            raise

    def clicks(self, loc, index):
        try:
            elements = self.find_elements(loc)
            logging.info('Click element by %s: %s' % (loc[0], loc[1]))
            elements[index].click()
            # time.sleep(1)
        except AttributeError:
            raise

    def set_value(self, loc, text, need_clear=False, need_hide_keyboard=False):
        try:
            element = self.find_element(loc)
            element.click()
            if need_clear:
                element.clear()
            logging.info('Send keys %s' % text)
            element.set_value(text)
            if need_hide_keyboard:
                self.click(self.btn)
        except AttributeError:
            raise

    def set_value_by_index(self, loc, text, index):
        try:
            element = self.find_elements(loc)[index]
            element.click()
            logging.info('Send keys %s' % text)
            element.set_value(text)
            self.click(self.btn)
        except AttributeError:
            raise

    def get_attribute(self, loc, name):
        element = self.find_element(loc)
        return element.get_attribute(name)

    def is_display(self, loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(loc).is_display())
            return True
        except:
            return False

    def get_window_size(self):
        """获取屏幕的高度和宽度"""
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        return height, width

    def swipe_up(self):
        """向上滑动屏幕"""
        height, width = self.get_window_size()
        self.driver.swipe(width/2, height * 3/4, width/2, height * 1/4)

    def swipe_down(self):
        """向下滑动屏幕"""
        height, width = self.get_window_size()
        self.driver.swipe(width/2, height * 1/4, width/2, height * 3/4)

    def swipe_left(self):
        """向左滑动屏幕"""
        height, width = self.get_window_size()
        self.driver.swipe(width * 3/4, height/2, width * 1/4, height/2)

    def swipe_right(self):
        """向右滑动屏幕"""
        height, width = self.get_window_size()
        self.driver.swipe(width * 1/4, height/2, width * 3/4, height/2)

    def get_screenshot(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        shot_path = os.path.join(base_dir, 'reports/screenshot')
        if not os.path.isdir(shot_path):
            os.makedirs(shot_path)
        pic_name = 'screenshot_' + time.strftime('%Y%m%d%H%M%S') + '.png'
        pic_url = os.path.join(shot_path, pic_name)
        try:
            self.driver.get_screenshot_as_file(pic_url)

            print('screenshot_name:%s' % pic_url)
        except:
            raise

    # 获取当前activity的名称
    def get_current_activity_name(self):
        activity_name = self.driver.current_activity
        print('Current activity name is: %s' % activity_name)
        return activity_name

    def find_element_by_scroll(self, loc):
        isSwipe = True
        i = 0
        while isSwipe and i < 5:
            try:
                self.driver.find_element(loc).click()
                isSwipe = False
            except Exception as e:
                self.swipe_up()
                time.sleep(1)
                i += 1

    def click_back_key(self):
        logging.info('Click device back key...')
        self.driver.keyevent(4)
        time.sleep(1)

    def swipe_up_by_element(self, loc):
        element = self.find_element(loc)
        start_x = element.rect['x'] + (element.rect['width'] / 2)
        start_y = element.rect['y']
        end_x = element.rect['x'] + (element.rect['width'] / 2)
        end_y = element.rect['y'] + (element.rect['height'])
        self.driver.swipe(end_x, end_y, start_x, start_y)
        time.sleep(1)

    def swipe_down_by_element(self, loc):
        element = self.find_element(loc)
        start_x = int(element.rect['x'] + (element.rect['width'] / 2))
        start_y = int(element.rect['y'])
        end_x = int(element.rect['x'] + (element.rect['width'] / 2))
        end_y = int(element.rect['y'] + (element.rect['height']))

        self.driver.execute_script("mobile:dragFromToForDuration",
                              {"duration": 0.5, "element": None, "fromX": start_x, "fromY": start_y, "toX": end_x, "toY": end_y})
        # self.driver.swipe(start_x, start_y, end_x, end_y)
        time.sleep(1)

    def drag_up(self):
        """for ios"""
        height, width = self.get_window_size()
        # width/2, height * 3/4, width/2, height * 1/4
        self.driver.execute_script("mobile:dragFromToForDuration",
                              {"duration": 0.5, "element": None, "fromX": width/2, "fromY": height * 3/4, "toX": width/2, "toY": height * 1/4})
        time.sleep(2)

    def drag_down(self):
        """for ios"""
        height, width = self.get_window_size()
        # self.driver.swipe(width/2, height * 1/4, width/2, height * 3/4)
        self.driver.execute_script("mobile:dragFromToForDuration",
                              {"duration": 0.5, "element": None, "fromX": width/2, "fromY": height * 1/4, "toX": width/2, "toY": height * 3/4})
        time.sleep(2)
