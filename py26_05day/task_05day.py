"""
============================
Author:柠檬班-木森
Time:2019/12/31
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
print("--------------------------第1题-----------------------------")
"""
一、现在有一个列表 li2=[1，2，3，4，5]，
     第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]，
     第二步：对列表进行升序排序 （从小到大）
     第三步：将列表复制一份进行降序排序（从大到小）
"""
li2 = [1, 2, 3, 4, 5]
# 第一步
li2.insert(0, 0)  # 在最前面加入0
li2[4] = 66
li2.extend([11, 22, 33])  # 在最后加入三个元素


print(li2)
# 第二步：从小到大排序
li2.sort()
print(li2)
# 第三步：从大到小排序
li3 = li2.copy()
li3.sort(reverse=True)
print(li3)
print("--------------------------第2题-----------------------------")
"""
二、定义一个空列表user=[],   分别提示用户输入，姓名，年龄，身高，用户输入完之后，
将输入的信息作为添加的列表中保存，然后按照一下格式输出：
    用户的姓名为：xxx,年龄为：xxx,  身高为：xxx  ,请仔细核对（要求：输出的身高要求保留2位小数）

"""
user = []
name = input("请输入姓名：")
age = input("请输入年龄：")
height = input("请输入身高：")
user.extend([name, age, height])
print('用户的姓名为：{},年龄为：{},身高为：{:.2f},请仔细核对'.format(name, age, float(height)))

print("--------------------------第3题-----------------------------")
"""
三、有下面几个数据 ，
t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",11)]
请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":22,"bb":22}
要注意字典中元素的顺序（使用python3.5以下的同学不用考虑位置）
"""
t1 = ("aa", 11)
t2 = ('bb', 22)
li1 = [("cc", 11)]
# 将t1,t2添加到li中
li1.append(t2)
li1.insert(0, t1)
# 转换为字典
dic = dict(li1)
# 修改CC的值
dic['cc'] = 22
print(dic)

print("--------------------------第4题-----------------------------")
"""
四、有5道题（通过字典来存储数据）： 某比赛需要获取你的个人信息，设计一个程序， 
 1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
 2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
 3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 
 4、平台为了保护你的隐私，需要你删除你的联系方式；
 5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
"""
name = input('请输入姓名：')
gender = input('请输入性别:')
age = input('请输入年龄：')
user_info = dict(
    name=name,
    gender=gender,
    age=age
)
print('当前信息如下:', user_info)

# 2、个人介绍
print('我的名字:{}，今年{}岁，性别:{}，喜欢敲代码'.format(name, age, gender))

# 3、添加信息
user_info['height'] = input('请输入身高：')
user_info['phone'] = input('请输入联系方式：')
print('当前信息如下:', user_info)

# 4、删除联系方式
user_info.pop('phone')
print('删除联系方式后信息如下:', user_info)

# 5、添加擅长技能
user_info["skill"] = input('请输入擅长技能:')
print('添加技能后信息如下:', user_info)

print("--------------------------第5题-----------------------------")
"""
五、请指出下面那些为可变类型的数据，那些为不可变类型的数据
1、 (11)    
2、 "111"
3、 ([11,22,33])
4、 {"aa":111}

答：可变的有 3,4，不可变的为1,2
"""

print("--------------------------第6题-----------------------------")
"""
6、请获取下面数据中的token，和reg_name
"""
data = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 74711,
        "leave_amount": 29600.0,
        "mobile_phone": "13367899876",
        "reg_name": "小柠檬666",
        "reg_time": "2019-12-13 11:12:53.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2019-12-30 22:28:57",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc0NzExLCJleHAiOjE1Nzc3MTYxMzd9.eNMtnEWr57iJoZRf2IRsGDWm2GKj9LZc1J2SGRprAwOk7EPoJeXSjJwdh0pcVVJygHmsbh1TashWqFv1bvCVZQ"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}
# 获取token
token = data["data"]["token_info"]["token"]
# 获取reg_name
reg_name = data["data"]["reg_name"]
print("token:{},regname:{}".format(token, reg_name))

print("--------------------------第7题-----------------------------")
"""
7、切片 
   1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9] 
   2、s = 'python java php',通过切片获取: java
   3、tu = ('a','b','c','d','e','f','g','h'),通过切片获取 ['g','b']
"""
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res1 = li[2::3]
s = 'python java php'
res2 = s[7:11]
tu = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
# 注意切出来是个元祖，要转换为列表
res3 = list(tu[-2:-8:-5])
print(res1, res2, res3)

print("--------------------------第8题-----------------------------")
"""
8、请分别列出学过的字符串方法，列表的方法、字典的方法、元祖的方法，并指出方法的作用

# --------------字符串的方法--------
join:字符串拼接
format:格式化输出
replace:替换
split:分割
upper:将小写字母转换为大写
lower:将大写字母转换为小写
find:查找元素的下标位置
count:查找某个元素出现的次数
# --------------列表的方法----------
append:往列表中最佳一个元素
insert:指定位置插入元素
extend:一次添加多个元素
pop:删除指定下标的元素
remove:删除指定的元素
clear:清空列表
index:查找元素的下标位置
count：查找某个元素出现的次数
sort：排序
reverse:反序（倒序）
copy:复制
# --------------字典的方法----------
pop:通过键删除指定的键值对
popitem：删除字典中最后一个键值对
update:一次往字典中添加多个键值对
get:通过键查找元素
keys:获取字典所有的键
values:获取字典所有的值
items:获取字典所有的键值对

# --------------元祖的方法----------
index:查找元素的下标位置
count查找某个元素出现的次数

"""
