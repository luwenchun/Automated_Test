"""
============================
Author:柠檬班-木森
Time:2020/1/3   20:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
集合的表示：{value,value.....}
# 空集合的定义：set()


# 集合的特性：
1、集合中只能存放不可变类型的数据（可以用来区分可变类型数据和不可变类型数据）
2、集合中不能存在重复的元素(可以用来对数据进行去重处理)
3、集合中的数据是无序的




"""

# 空字典
# dic = {}
# print(type(dic))


# 空集合：
# s = set()
# print(type(s))


# s1 = {1, 2, 3}
# print(type(s1))
#  区分数据可变不可变
# s = {1, "1213", (1, 2, 3), {1, 2, 3}}


# 对列表，元组进行去重
# li = [11, 22, 11, 22, 33, 11, 22, 33, 5, 6, 3, 63, 6, 22, 3, 3]
# 将列表转换为集合
# s2 = set(li)
# print(s2)
# li = list(s2)
# print(li)

# 集合中不能存在重复元素，定义的时候写再多的重复元素都会自动清除
# s3 = {1, 2, 3, 4, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 3, 3, 2, 3, 4}
# print(s3)


# 集合的相关操作方法：
# 添加数据:add
# 删除数据：pop  remove


# li = {'a','v','5','d','q'}

# 随机位置添加一个元素
# li.add(999)

# 随机删除一个元素
# li.pop()

# 删除指定的元素
# li.remove("d")

# print(li)


# s = "caaaaaaaaghjklvbhnm"
# li = list(s)
# li = list(set(li))
# s = ''.join(li)


# s = ''.join(list(set(list(s))))
# print(s)


# 集合的 交集 并集  差集


a = {1, 2, 3, 11, 22}

b = {11, 22, 33, 44, 55, 1}

# 交集: &
# s = a & b
# print(s)


# 并集 |
# ss = a | b
# print(ss)


# 差集 -
# s1 = a - b
# print(s1)

# s2 = b - a
# print(s2)


