# -*- encoding=utf8 -*-
__author__ = "jiou"

from airtest.core.api import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.cli.parser import cli_setup
from open_APP import *
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/5ffec876",
    ])


def info_keyword(KeyWord):
    #在首页输入框输入搜索关键字方法
    #调用启动APP的方法
    open_APP("com.xiaomi.shop")
    #启动后等待页面完全加载完毕
    wait(Template(r"tpl1573531986451.png", record_pos=(-0.39, 0.136), resolution=(1080, 2340)))
    #点击首页搜索框进行二级页面
    poco("com.xiaomi.shop.plugin.homepage:id/fragment_search_swither").click()
    #将光标定位在二级页面的输入框中
    poco("com.xiaomi.shop2.plugin.search:id/input").click()
    #输入文本
    text(KeyWord)
    #点击搜索按钮
    poco("com.xiaomi.shop2.plugin.search:id/search_fragment_search_btn").click()


info_keyword("耳机")