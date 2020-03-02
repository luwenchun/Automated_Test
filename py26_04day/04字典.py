"""
============================
Author:柠檬班-木森
Time:2019/12/30
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
字典: 
字典的定义：使用{}来表示字典，每一个元素都是有一个键值对(key:value)组成

字典中的数据规范：
key:不能重复，只能是不可变类型的数据（字符串，数值，元祖），建议key都使用字符串。
value:可以是任意类型的数据

字典定义的两种方法：
第一种
user_info = {"name": "木森", "age": 18, "gender": "男"}
第二种
user_info = dict(name="木森",age=18,gender="男")


"""

# user_info = ("木森", 18, "男")
# name = user_info[0]
# print(name)
# -------字典的定义-----------------
# 第一种
# user_info = {"name": "木森", "age": 18, "gender": "男"}
# 第二种
# user_info = dict(name="木森",age=18,gender="男")
# print(user_info,type(user_info))

# 第三种
# data = [("name", "木森"), ("age", 18), ("gender", "男")]
# user_info2 = dict(data)
# print(user_info2)

#
# name = user_info["name"]
# print(name)
# print(user_info["age"])
# print(user_info["gender"])

# 如果有重复的key,那么就会把原来key所对应的值该覆盖掉
# dic = {"a": 11, "a": 111, "a": 1111}
# print(dic)
