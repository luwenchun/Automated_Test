"""
============================
Author:柠檬班-木森
Time:2020/3/11   22:09
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
深浅复制：只在数据嵌套的情况下讨论（列表嵌套列表的情况下）





"""

from copy import deepcopy

li = [11, 22, 33]

list1 = [1, 2, 3, li]

# 浅拷贝
# list2 = list1.copy()

# print(list1, id(list1))
# print(list2, id(list2))

# li.append(999)
#
# print(list1, id(list1))
# print(list2, id(list2))

# 深度拷贝

list4 = deepcopy(list1)
print(list1, id(list1))
print(list4, id(list4))

li.append(999)

print(list1, id(list1))
print(list4, id(list4))
