# -*- encoding=utf8 -*-
__author__ = "jiou"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/192.168.8.189:5555",
    ])

def star():
    #点击底部星球导航栏
    poco("com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_discovery_icon").click()


def module():
    #在星球页面从右向左滑动到视频模块
     swipe((850,1557),(32,1231))
        
def recommend():
    #从左向右滑动到推荐模块
     swipe((270,1315),(1050,1350))
        
        
def Refresh():
    #下拉刷新
    swipe((543,855),(570,2086))
    
Refresh()