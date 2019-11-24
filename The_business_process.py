# -*- encoding=utf8 -*-
__author__ = "root"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import unittest
from open_APP import *
from input_KeyWord import *
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/5ffec876",
    ])

#业务流程 打开APP后 在首页搜索框输入 关键字
#点击一个搜索到的商品查看详情 点击收藏
class p1(unittest.TestCase):
    def test_01(self):
        #打开APP
         open_APP("com.xiaomi.shop")
            
    def test_02(self):
        #点击首页输入框
        search()
        
    def test_03(self):
        #输入搜索关键字
        info_keyword("手机")
        
    def test_04(self):
        #点击查看一个搜索商品的详情
        poco(text="小米CC9 Pro").click()
        
    def test_05(self):
        #点击收藏
        poco("com.xiaomi.shop2.plugin.goodsdetail:id/fav_icon").click()
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
