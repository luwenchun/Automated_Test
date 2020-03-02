"""
============================
Author:柠檬班-木森
Time:2020/2/21   21:49
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
import random
import os
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.handlepath import DATADIR
from common.handleconfig import conf
from common.handlerequests import SendRequest
from common.handlelog import log

case_file = os.path.join(DATADIR, "apicases.xlsx")


@ddt
class TestRecharge(unittest.TestCase):
    excel = ReadExcel(case_file, "recharge")
    cases = excel.read_data()
    request = SendRequest()

    @classmethod
    def setUpClass(cls):
        pass
        # 这个方法在该测试用例类的用例执行之前会执行
        # 在这个方法里进行登录
        # 提取token,保存为类属性

    @data(*cases)
    def test_recharge(self, case):
        # 第一步：准备用例数据
        url = conf.get("env", "url") + case["url"]
        method = case["method"]
        data = eval(case["data"])
        headers = eval(conf.get("env", "headers"))
        # 在请求头中加入setupclass中提取出来的token

        expected = eval(case["expected"])
        row = case["case_id"] + 1
        # 第二步：发送请求，获取结果
        response = self.request.send(url=url, method=method, json=data, headers=headers)
        res = response.json()
        # 第三步：断言（比对预期结果和实际结果）
        # 作业不要求对充值进行断言。


"""
自动化的覆盖率问题









"""
