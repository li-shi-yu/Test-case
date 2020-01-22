# -*- encoding=utf8 -*-
__author__ = "shiyu.li"

import os
from airtest.core.api import *
from airtest.core.android.adb import *
from airtest.core.android.android import *
from poco.proxy import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco()
adb = ADB()
android = Android()

def get_deviceList():

    deviceList = os.getenv("device")
    print(device_list)
    return deviceList

def check_app(package):
    
    # adb shell dumpsys package com.zen.zbike
    output = adb.shell(['dumpsys', 'package', package])
    pattern = r'Package\s+\[' + str(package) + '\]'
    match = re.search(pattern, output)
    if match is None:
        return False
        # raise AirtestError('package "{}" not found'.format(package))
    return True

def start(package, install_path):
    
    try:
        if android.check_app(package):
            clear_app(package)
        else:
            try:
                install(install_path)
            except:
                print('FAILED')
    except:
        install(install_path)
                
    clear_app(package)
    start_app(package)

def stop(package):
    
    clear_app(package)
    stop_app(package)
    
def exists(value):
    try:
        return element.attr('visible')
    except:
        return False
    
def assert_exists(img, msg='test'):

    try:
        pos = loop_find(Template(img), timeout=ST.FIND_TIMEOUT, threshold=ST.THRESHOLD_STRICT)
        return pos
    except TargetNotFoundError:
        raise AssertionError("%s does not exist in screen, message: %s" % (img, msg))

def UItouch(img):

    assert_exists(img)
    touch(Template(img, record_pos=(0.292, 0.027), resolution=(1080, 2220)))

def click(element, timeout = 60):
    
    poco(element).wait_for_appearance(timeout)
    try:
        poco(element).click()
    except():
        print('An exception occured!')

# 设置UI元素的属性        
def set_text(element, content):
    
    try:
        poco(element).set_text(content)
    except:
        print('An exception occured!')
        
# adb shell的命令去发送广播，然后有一个listener要接收这个广播
def sendKeys(content):
    
    try:
        text(content)
    except:
        print('An exception occured!')
        