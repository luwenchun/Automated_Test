"""
============================
Author:柠檬班-木森
Time:2020/3/9   21:00
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest


class Case:
    pass


c = Case()
import requests

class TestClass(unittest.TestCase):

    def test_01(self):
        self.assertIsInstance(c, Case)

    def test_02(self):
        li = [1, 2, 3]
        li2 = [1, 2, 3, 4, 5]
        # 不能这样对两个列表进行成员判断
        # self.assertIn(li, li2)
        dic = {"a": 1}
        dic2 = {"a": 2, "b": 1}
        self.assert_dict_items(dic, dic2)

    def assert_dict_items(self, dic1, dict2):
        """
        对字典进行成员断言
        :param dic1: 字典
        :type dic1:dict
        :param dict2:
        :type dict2:dict
        :return:
        """
        for i in dic1.items():
            if i not in dict2.items():
                raise AssertionError("{} not in {}".format(dic1, dict2))
