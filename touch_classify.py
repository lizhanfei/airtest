# -*- encoding=utf8 -*-
__author__ = "jiou"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/5ffec876",
    ])



def classify(text):
    #点击底部分类导航栏
        poco("com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_category_icon").click()
    #点击分类
    #抛异常
    try:
        #如果找到该分类就点击
        poco(text=text).click()
        #如果找不到就向下滑动屏幕 继续找
    except Exception as e:
        swipe((100,1969),(137,320))
        poco(text=text).click()


classify("服务")