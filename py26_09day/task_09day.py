"""
============================
Author:柠檬班-木森
Time:2020/1/10   22:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# 第一题：现有数据如下
# users_title = ["name", "age", "gender"]
# users_info = [['小明', 18, '男'], ["小李", 19, '男'], ["小美", 17, '女']]

# # 要求：将上述数据转换为以下格式
# users = [{'name': '小明', 'age': 18, 'gender': '男'},
#          {'name': '小李', 'age': 19, 'gender': '男'},
#          {'name': '小美', 'age': 17, 'gender': '女'}]

users_title = ["name", "age", "gender"]
users_info = [['小明', 18, '男'], ["小李", 19, '男'], ["小美", 17, '女']]

# 定义一个列表用来存放转换之后的数据
users = []
# 遍历user_info中的数据
for info in users_info:
    # 把user_title和user_info进行聚合打包
    data = zip(users_title, info)
    # 转换为字典，添加到列表users中
    users.append(dict(data))

print(users)

# 第二题：请封装一个函数，按要求实现数据的格式转换
# 传入参数： data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# 返回结果：res = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]
# 通过代码将传入参数转换为返回结果所需数据，然后返回
li = ["{'a':11,'b':2}", "[11,22,33,44]"]


def work2(data):
    # 创建一个新列表
    new_data = []
    # 遍历列表中的数据
    for i in data:
        # 将数据使用eval进行转换
        res = eval(i)
        # 将将转换后的数据放入新列表
        new_data.append(res)
    # 返回转换后的数据
    return new_data


res = work2(li)
print("转换之后的结果为:", res)

# 第三题：简单题
# 	1、什么是全局变量？
# 	2、什么是局部变量？
# 	3、函数内部如何修改全局变量（声明全局变量 ）？
#   4、写出已经学过的所有python关键字，分别写出用途？

"""
答案：
1、直接定义在py文件（模块）中的变量叫做全局变量，全局变量在该模块中任意地方都可以访问
2、定义在函数中的变量，叫做局部变量，局部变量只有在该函数内部才能访问
3、在函数中定义（或修改）全局变量，需要使用global进行声明
4、已经学过的python关键字
学过的：20个
False:bool数据类型
True :bool数据类型
None :表示数据为空

and: 逻辑运算符：与 
or:  逻辑运算符：或
not:  逻辑运算符：非

is  :身份运算符 
in  :成员运算符
del :删除数据
pass :表示通过（一般用来占位的）

if    : 条件判断
elif  : 条件判断
else : 条件判断

while  :条件循环
for    :遍历循环
break  :用来终止循环的
continue :中止当前本轮循环  开启下一轮循环

def  ：定义函数
return ：函数返回值
global  ：定义全局变量

"""
