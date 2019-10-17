import unittest

import ddt

from ECShop.common.create_data import CreateData
from ECShop.script.regdit_flow import RegditFlow

_datas = [i for i in range(1,5)]
@ddt.ddt
class ECShopRegdit(unittest.TestCase):
    # 没次执行前都执行一次
    def setUp(self):
        self.regflow = RegditFlow()  # 实例化之前封装的RegditFlow类的对象

    # 每次用例执行后都关闭浏览器
    def tearDown(self):
        self.regflow.reg_page.close_browser()
    @ddt.data(*_datas)
    def test_case_01(self,data):
        # global 后面可以跟一个或多个变量名
        global _data, _a, _b, _username, _password, _email, _phone, \
            _qustion, _answer, _answer_cn, _data_info
    # 调用注册流程
    _data_path =r'E:\ECShop\ECShop\data\regdit_data.xlsx'
    _a = CreateData()
