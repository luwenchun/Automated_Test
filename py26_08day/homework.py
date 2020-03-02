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
# lists=[]
# for item in users_info:
#     res = zip(users_title, item)
#     lists.append(dict(res))
# print(lists)


# 第二题：请封装一个函数，按要求实现数据的格式转换
# 传入参数： data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# 返回结果：res = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]
# 通过代码将传入参数转换为返回结果所需数据，然后返回
# def famate(lists):
#     list=[]
#     for item in lists:
#        list.append(eval(item))
#     return list
#
# data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# res=famate(data)
# print(res)

# 第三题：简单题
#  1、什么是全局变量？
# 直接定在在模块中的变量，在该模块中任何地方都可以直接访问（使用）
#  2、什么是局部变量？
# 定义在函数内部的变量，只能在定义的那个函数内部使用
#  3、函数内部如何修改全局变量（声明全局变量 ）？
# 在函数内部修改全局变量的值：使用global进行声明
#   4、写出已经学过的所有python关键字，分别写出用途？

li1 = ["page{}".format(i) for i in range(1, 5)]
print(li1)
