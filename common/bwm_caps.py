# coding=utf-8
import sys, os
import yaml
import logging
import logging.config
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
base_dir = os.path.dirname(os.path.dirname(__file__))
log_file_path = os.path.join(base_dir, 'config/log.conf')
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()


def bwm_desired():
    fwd_caps_path = os.path.join(base_dir, 'config/bwm_caps.yaml')
    with open(fwd_caps_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    desired_caps = {
        "platformName": data["platformName"],
        "platformVersion": data["platformVersion"],
        "deviceName": data["deviceName"],
        "udid": data["udid"],
        "app": data["app"],
        "noReset": data["noReset"],
        "automationName": data["automationName"],
        "useNewWDA": data["useNewWDA"],
        "commandTimeouts": data["commandTimeouts"],
        "newCommandTimeout": data["newCommandTimeout"]
    }

    logging.info("Start APP.")
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    return driver


if __name__ == '__main__':
    bwm_desired()

