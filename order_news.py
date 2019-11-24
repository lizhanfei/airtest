# -*- encoding=utf8 -*-
__author__ = "root"

from airtest.core.api import *

from info_seckill import *
from open_APP import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/127.0.0.1:21503?cap_method=JAVACAP",
            "Android://127.0.0.1:5037/5ffec876?cap_method=JAVACAP",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


    
def order(data):
    #启动APP
    open_APP("com.xiaomi.shop")
    #首页滑动到秒杀模块
    seceli()
    #点击进入秒杀模块
    seckill()
    #点击选择场次
    poco(text=data).click()
    #点击抢购
    poco("android:id/content").child("android:id/primary").child("android:id/primary").offspring("com.xiaomi.shop.plugin.instantpurchase:id/flash_viewpager").offspring("com.xiaomi.shop.plugin.instantpurchase:id/flash_list").child("android.widget.LinearLayout")[4].offspring("com.xiaomi.shop.plugin.instantpurchase:id/flash_product_btn").click()
    #加入购买
    poco("android.widget.Button").click()
    #结算
    poco("com.xiaomi.shop2.plugin.shopcart:id/next").click()
    