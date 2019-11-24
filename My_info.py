# -*- encoding=utf8 -*-
__author__ = "root"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/5ffec876?cap_method=JAVACAP",
    ])


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
# script content
def my_info():
    #点击底部导航栏我的模块
    poco("com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_mine_icon").click()
def my_order():
    #点击全部订单列表
    poco(text="全部订单").click()




