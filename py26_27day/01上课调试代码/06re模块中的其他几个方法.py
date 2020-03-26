"""
============================
Author:柠檬班-木森
Time:2020/2/28   20:13
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
findall：返回的是所有符合规范的数据，放在在一个列表中
search:匹配出第一个符合规范的数据，返回的是一个匹配对象
    group（）可以获取匹配到数据

search:从字符串的头部匹配出规范的数据，返回的是一个匹配对象(如果数据不在字符串头部，是匹配不到的)
"""

import re

s = "123#python#1234#python#11111#pwd#python"

# res = re.findall("python",s)
# res = re.search("#(python)#1234#(python)#11111#(pwd)#",s)
# print(res)
# print(res.group())
# print(res.group(1))
# print(res.group(2))
# print(res.group(3))

# macth
# # res= re.match(r"1234",s)
# # # print(res)

# sub：替换的方法
# res = re.sub("#.+?#","java",s)
# print(res)