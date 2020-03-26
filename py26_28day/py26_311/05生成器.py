"""
============================
Author:柠檬班-木森
Time:2020/3/11   21:49
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
# import openpyxl
#
#
# wb = openpyxl.load_workbook("cases.xlsx")
# sh = wb["register"]
# res = sh.rows
# print(res)
#
# print(next(res))
# print(next(res))
#
# print(res.send(11))

"""
生成器（generator）：生成器是一种特殊的迭代器
生成器比迭代器多个几个方法：
send():和生成内部进行数据交互


生成器的定义：
第一种：生成器表达式

第二种：生成器函数
    只要函数中定义yield这个关键字，那么这个函数就不再是一个普通的函数了，而是一个生成器函数
    生成器函数在调用时，会自动返回一个生成器对象


"""

# 生成器表达式
# g1 = (i for i in range(10))
# print(g1)


# 生成器函数
def gen():
    print("-----开始执行------")
    for i in range(10):
        res = yield i
        print("res的值：",res)



g2 = gen()

# print(g2)

print(next(g2))
print(next(g2))
print(next(g2))
print(g2.send(100))


