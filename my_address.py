# -*- encoding=utf8 -*-
__author__ = "root"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:21503",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

def touch_More_and_more():
    #点击我的模块更多功能
    poco(text="更多功能").click()

def address():
    #点击收获地址
    poco(text="收货地址").click()
address()    
