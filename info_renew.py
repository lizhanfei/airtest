# -*- encoding=utf8 -*-
__author__ = "root"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:21503?cap_method=JAVACAP",
    ])
def touch_renew():
    #点击首页以旧换新模块

    touch(Template(r"tpl1574340670879.png", rgb=True, record_pos=(-0.196, 0.014), resolution=(800, 1200)))
    
    
def phone():
    #点击以旧换新内的手机模块
    touch(Template(r"tpl1574340982990.png", record_pos=(-0.365, 0.0), resolution=(800, 1200)))
   

