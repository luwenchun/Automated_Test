"""
============================
Author:柠檬班-木森
Time:2020/3/11   21:21
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
# import unittest
# from ddt import data, ddt
#
#
# @ddt
# class MyTest(unittest.TestCase):
#
#     @data(11,22,33)
#     def test_01(self):
#         pass


"""
装饰器的作用：在不修改原功能代码的基础上，给代码扩展新的功能。



"""

print()

def func(fu):
    def wrapper():
        print("-------------开始执行-------------")
        fu()
        print("--------------执行完毕----------")
    return wrapper



# 打印两个数之和
@func      # -->   add = func(add)
def add():
    a = 100
    b = 200
    print("a+b:", a + b)


add()
