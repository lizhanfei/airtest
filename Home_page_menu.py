# -*- encoding=utf8 -*-
__author__ = "root"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP&&ori_method=ADBORI",
    ])
def touch_menu(page):
    #点击首页分类菜单
    poco("android:id/content").child("android:id/primary").child("android:id/primary").offspring("com.xiaomi.shop.plugin.homepage:id/main_container").child("android:id/primary").offspring("android:id/list").child("android.widget.RelativeLayout")[0].child("android.widget.ImageView")[page].click()
   
     
def inquiry():
    #输入首页分类菜单的索引
    i  = input("输入0到4的数字:")
    #传给touch_menu
    touch_menu(int(i))
inquiry()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)