"""
============================
Author:柠檬班-木森
Time:2020/3/11   21:40
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
可迭代对象(iterable)：只要可以通过for循环进行遍历的都叫可迭代对象


迭代器(iterator)：能够使用next函数取值
    所有的可迭代对象都可以使用内置函数iter()转换为迭代器


"""
li = [11,22,33]


li2 = iter(li)

# print(next(li2))
# print(next(li2))
# print(next(li2))
# print(next(li2))
# for i in li2:
#     print(i)


