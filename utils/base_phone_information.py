# coding=utf-8

import subprocess


def get_device_udid():
    result = subprocess.Popen("idevice_id -l", shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()

    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]


def get_device_name():
    cmd = 'ideviceinfo -k DeviceName'
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]


def get_device_version():
    cmd = 'ideviceinfo -k ProductVersion'
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]


if __name__ == '__main__':
    print(get_device_udid())
