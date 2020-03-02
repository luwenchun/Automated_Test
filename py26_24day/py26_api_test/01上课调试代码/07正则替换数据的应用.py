"""
============================
Author:柠檬班-木森
Time:2020/2/28   20:28
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import re
from common.handleconfig import conf


# s = '{"mobile_phone":"#phone#","pwd":"#pwd#","type":1,"reg_name":"#reg_name#"}'

# 使用字符串的替换方法进行替换
# s = s.replace("#phone#", conf.get("test_data", "phone"))
# s = s.replace("#pwd#", conf.get("test_data", "pwd"))
#
# print(s)

# r1 = r"#(.+?)#"
#
# res = re.search(r1,s)
# data = res.group()
# key = res.group(1)
# # print(key)
# # print(data)
# s = s.replace(data,conf.get("test_data",key))
# print(s)
#
# res = re.search(r1,s)
# data = res.group()
# key = res.group(1)
# s = s.replace(data,conf.get("test_data",key))
# print(s)
#
#
# res = re.search(r1,s)
# data = res.group()
# key = res.group(1)
# s = s.replace(data,conf.get("test_data",key))
# print(s)


def replace_data(s):
    r1 = r"#(.+?)#"
    while re.search(r1, s):
        res = re.search(r1, s)
        data = res.group()
        print("data:",data)
        key = res.group(1)
        print("key",key)
        s = s.replace(data, conf.get("test_data", key))
    return s


s = '{"mobile_phone":"#phone#","pwd":"#pwd#","type":1,"reg_name":"#reg_name#"}'

s = replace_data(s)
print(s)
