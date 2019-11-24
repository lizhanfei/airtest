# -*- encoding=utf8 -*-
__author__ = "jiou"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android:///",
    ])


# script content


def open_APP():
    #启动app的方法
    start_app("com.xiaomi.shop")

open_APP()
