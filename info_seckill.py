# -*- encoding=utf8 -*-
__author__ = "root"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:21503?cap_method=JAVACAP",
    ], project_root="C:/Users/root/Desktop/APP_ui")


# script content
print("start...")

def slide():
    #首页滑动到秒杀位置
    for i in range(2):
        swipe(Template(r"tpl1574423383378.png", record_pos=(-0.071, 0.036), resolution=(800, 1200)), vector=[-0.0494, -0.4076])
        


def touch_seckill():
    #点击秒杀模块
    touch(Template(r"tpl1574423709434.png", record_pos=(-0.026, -0.281), resolution=(800, 1200)))
    
def shopping():
    #点击秒杀里的购物车
    touch(Template(r"tpl1574423827871.png", record_pos=(0.469, -0.671), resolution=(800, 1200)))

    





