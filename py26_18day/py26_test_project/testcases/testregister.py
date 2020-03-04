"""
============================
Author:柠檬班-木森
Time:2020/2/14   20:15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import os
import unittest
from py26_18day.py26_test_project.library.ddt import ddt, data
from py26_18day.py26_test_project.common.readexcel import ReadExcel
from py26_18day.py26_test_project.register import register
from py26_18day.py26_test_project.common.handlelog import log
from py26_18day.py26_test_project.common.handlepath import DATADIR


@ddt
class TestRegister(unittest.TestCase):
    excel = ReadExcel(os.path.join(DATADIR,"cases.xlsx"), "register")
    cases = excel.read_data()

    @data(*cases)
    def test_register(self, case):
        # 第一步：准备数据
        data = eval(case["data"])
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        # 第二步：调用函数获取实际结果
        res = register(*data)
        print('11111',*data)
        # 第三步：比对数据
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            self.excel.write_data(row=row, column=5, value="未通过")
            log.error("用例 {} 执行未通过".format(case["title"]))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=5, value="通过")
            log.info("用例 {} 执行通过".format(case["title"]))