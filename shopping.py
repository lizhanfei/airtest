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

def touch_shopping():
    #点击底部购物车导航栏
    poco("com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_cart_icon").click()
    
def shopping_Refresh():
    #购物车下拉刷新
    swipe((540,312),(470,1799))

def compile():
    #点击购物车编辑按钮
    touch(Template(r"tpl1573878716549.png", record_pos=(0.353, -0.923), resolution=(1080, 2340)))
   


