"""
============================
Author:柠檬班-木森
Time:2020/3/2   21:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
import random
import os
import jsonpath
from library.ddt import ddt, data
from common.readexcel import ReadExcel
from common.handlepath import DATADIR
from common.handleconfig import conf
from common.handlerequests import SendRequest
from common.handlelog import log

from common.connectdb import DB
from common.handle_data import replace_data, CaseDate

"""
投资接口：
1、需要有标：管理员登录，加标、审核，
2、用户登录
3、投资用例的执行

# 关于投资的sql校验语句
1、用户表、校验用户余额是否发生变化，变化金额等于所投金额（根据用户id去查member表）
2、根据用户id和标id去投资表中查用户的投资记录，（invest里面查用户对应的标是否新增一条记录）
3、根据用户id去流水标中查询流水记录（查询用户投资之后是否多了一条记录）
4、在刚好投满的情况下，可以根据投资记录的id，去回款计划表中查询是否，生成回款计划。


"""
case_file = os.path.join(DATADIR, "apicases.xlsx")


@ddt
class TestLogin(unittest.TestCase):
    excel = ReadExcel(case_file, "invest")
    cases = excel.read_data()
    request = SendRequest()

    @data(*cases)
    def test_login(self, case):
        # 第一步：准备用例数据
        url = conf.get("env", "url") + case["url"]
        method = case["method"]
        case["data"] = replace_data(case["data"])
        data = eval(case["data"])
        headers = eval(conf.get("env", "headers"))
        # 判断是否是登录接口，不是登录接口则需要添加token
        if case["interface"] != "login":
            headers["Authorization"] = getattr(CaseDate, "token_value")

        expected = eval(case["expected"])
        row = case["case_id"] + 1
        # 第二步：发送请求，获取结果
        response = self.request.send(url=url, method=method, json=data, headers=headers)
        res = response.json()
        # 发送请求后，判断是否是登陆接口
        if case["interface"].lower() == "login":
            # 提取用户id保存为类属性
            CaseDate.member_id = str(jsonpath.jsonpath(res, "$..id")[0])
            token = jsonpath.jsonpath(res, "$..token")[0]
            token_type = jsonpath.jsonpath(res, "$..token_type")[0]
            # 提取token,保存为类属性
            CaseDate.token_value = token_type + " " + token
        # 判断是否是加标的用例，如果是的则请求标id
        if case["interface"] == "add":
            CaseDate.loan_id = str(jsonpath.jsonpath(res,"$..id")[0])
        # 第三步：断言（比对预期结果和实际结果）
        try:
            self.assertEqual(expected["code"], res["code"])
            # self.assertEqual(expected["msg"], res["msg"])
            self.assertIn(expected["msg"], res["msg"])


        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="未通过")
            log.error("用例：{}，执行未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="通过")
            log.info("用例：{}，执行未通过".format(case["title"]))
