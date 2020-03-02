# # 第一题：现有数据如下
# users_title = ["name", "age", "gender"]
# users_info = [['小明', 18, '男'], ["小李", 19, '男'], ["小美", 17, '女']]
#
# # 要求：将上述数据转换为以下格式
# users = [{'name': '小明', 'age': 18, 'gender': '男'},
#          {'name': '小李', 'age': 19, 'gender': '男'},
#          {'name': '小美', 'age': 17, 'gender': '女'}]

# users_title = ["name", "age", "gender"]
# users_info = [['小明', 18, '男'], ["小李", 19, '男'], ["小美", 17, '女']]
#
# def func():
#     users = []
#     for i in users_info:
#         new_info = zip(users_title,i)
#         users.append(dict(new_info))
#     print('users={}'.format(users))
# func()

# 第二题：请封装一个函数，按要求实现数据的格式转换
# # 传入参数： data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# # 返回结果：res = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]
# # 通过代码将传入参数转换为返回结果所需数据，然后返回

# def change(a):
#     res = []
#     for i in a:
#         res.append(eval(i))
#     return res
# data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# res_01=change(data)
# print(res_01)

# 第三题：简单题
#  1、什么是全局变量？
# 直接定在在模块中的变量，在该模块中任何地方都可以直接访问（使用）
#  2、什么是局部变量？
# 定义在函数内部的变量，只能在定义的那个函数内部使用
#  3、函数内部如何修改全局变量（声明全局变量 ）？
# 在函数内部修改全局变量的值：使用global进行声明
#   4、写出已经学过的所有python关键字，分别写出用途？
# import keyword
# aa = keyword.kwlist
# print(aa)
#
# 'False', 'None', 'True', 'and','break', 'continue', 'def', 'del',
# 'elif', 'else',  'for', 'from', 'global', 'if', 'import',
# 'in', 'is',  'not', 'or', 'pass',  'return', 'while',
#
# False: python中的布尔类型，与True相对。
# None:返回结果为none
# True:python中的布尔类型，与False相对。
# and:逻辑判断语句‘与’，and左右两边都为真，则判断结果为真，否则都是假。
# break:跳出循环语句。终止循环
# continue：跳出本次循环
# def:定义函数
# del：删除变量
# if 条件判断
# elif:条件分支语句
# else:与if连用，if else 条件分支语句
# for：遍历 如 for i in range(7)
# from：从...中（进行...）导入模块的变量或函数
# global:声明全局变量。在函数内部修改全局变量的值：使用global进行声明
# import:导包
# in：在...中，判断是否存在 成员运算符
# is:身份运算符
# not：逻辑操作符，非
# or：或者 一个真就为真
# pass：函数内，占位符
# return:函数返回值
# while:循环语句：可加条件，当符合条件就执行后面的代码
