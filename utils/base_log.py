# coding=utf-8

import logging
import os
import time
from functools import wraps

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Log:
    def __init__(self):
        log_dir = PATH("../logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # create handler,write log
        fh = logging.FileHandler(os.path.join(log_dir, time.strftime('%Y%m%d%H%M%S', time.localtime()) +
                                              '.log'), encoding='utf-8')
        # Define the output format of formatter handler
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        stream_handle = logging.StreamHandler()
        stream_handle.setFormatter(formatter)
        self.logger.addHandler(stream_handle)

    def get_logger(self):
        return self.logger


def logger(param, logging):
    def wrap(function):
        @wraps(function)
        def _wrap():
            logging.info("当前模块 {}".format(param))
            return function()
        return _wrap
    return wrap


if __name__ == '__main__':
    log = Log().get_logger()
    log.info('test log')
    log.error('failed')
