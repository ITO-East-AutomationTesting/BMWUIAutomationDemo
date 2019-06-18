# coding=utf-8
import os
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from utils.base_phone_information import *

base_dir = os.path.dirname(os.path.dirname(__file__))


def bwm_desired():
    fwd_caps_path = os.path.join(base_dir, 'config/bwm_caps.yaml')
    with open(fwd_caps_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    desired_caps = {
        "platformName": data["platformName"],
        "platformVersion": get_device_version(),
        "deviceName": get_device_name(),
        "udid": get_device_udid(),
        "app": data["app"],
        "noReset": data["noReset"],
        "automationName": data["automationName"],
        "useNewWDA": data["useNewWDA"],
        "commandTimeouts": data["commandTimeouts"],
        "newCommandTimeout": data["newCommandTimeout"]
    }
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    return driver


if __name__ == '__main__':
    bwm_desired()

