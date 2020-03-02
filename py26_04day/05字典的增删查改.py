"""
============================
Author:柠檬班-木森
Time:2019/12/30
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
字典的增删查改

1、添加元素
    通过键值对赋值
    update:一次添加多个元素


2、修改元素
    

3、删除元素
    pop
    popitem


4、查找元素
    get


5、其他的几个方法
    keys
    values
    items

python中的关键字：del
可以用来删除任何数据



"""

# dic = {"a": 11, "b": 22, "c": 33, "d": 11111}

# 1、添加元素
# 直接通过键去赋值(如果有这个键那就是修改这个键所对应的值)
# dic['aa'] = 999
# print(dic)

# update:一次往字典中添加多个键值对(将一个字典更新到原来的字典中)
# dic.update({"aa": 111, "bb": 222, "cc": 333})
# print(dic)

# 2、修改元素
# 直接通过键去赋值,修改这个键所对应的值
# dic['aa'] = 999
# print(dic)


# 3、删除元素
# # pop方法：通过键去删除对应的键值对,返回对应的value
# v = dic.pop('a')
# print(v)

# popitem: 删除字典中最后一个键值对
# dic.popitem()
# print(dic)

# 4、查找元素的方法

# dic = {"a": 11, "b": 22, "c": 33, "d": 11111}

# 通过键去找对应的值,如果键不存在会报错（KeyError）
# res1 = dic["aa"]
# print(res1)

# get方法,如果键不存在返回的是None
# res2 = dic.get("aa")
# print(res2)

# 其他的几个方法
# keys:获取字典中所有键,可以通过list转换为一个列表
# res3 = list(dic.keys())
# print(res3)

# values：获取字典中所有的值,可以通过list转换为一个列表
# res4 = list(dic.values())
# print(res4)

# items:获取字典中的键值对,可以通过list转换为一个列表
# res5 = list(dic.items())
# print(res5)


# 关键字del

# a = 100
# 1、删除变量
# del a
# print(a)

# li = [1, 2, 3]
# # 2、删除列表中的某个元素
# del li[0]
#
# print(li)

# dic2 = {"aa": 11, "bb": 22}
# # 3、删除字典中的某个键值对
# del dic2['aa']
# print(dic2)


li = [("name", "木森"), ("age", 18), ("gender", "男")]
# 获取下面数据中的木森
li2 = {"a": ["11", "22", ("python", "java", {"name": "木森"})]}

res1 = li2["a"]

res2 = res1[2]

res3 = res2[2]

print(res3["name"])