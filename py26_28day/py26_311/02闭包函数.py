"""
============================
Author:柠檬班-木森
Time:2020/3/11   21:14
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# 闭包函数
"""
1、函数中嵌套一个函数
2、外层函数返回的是内层函数的函数名
3、内层函数对外部作用域有非全局变量的引用（不能引用全局变量）
"""

b = 9999


def func():
    a = 100

    def wrapper():
        print(a * 2 + b)
        print("内部嵌套的函数")

    return wrapper
