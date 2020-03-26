"""
============================
Author:柠檬班-木森
Time:2020/3/11   21:01
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import json
import requests

"""
json模块

loads:将字符串中的json数据，转换为对应的python类型数据

dumps:将python数据转换为json数据，放在一个字符串中


"""

# res = requests.post(url="http://test.lemonban.com/futureloan/mvc/api/member/register")
# res1 = res.json()
#
# print(res1)


# # print(res.text,type(res.text))
# j_data = res.text
# print("j_data:",j_data,type(j_data))
#
# d_data = json.loads(j_data)
# print("d_data:",d_data,type(d_data))

# data1 = '{"status":false,"code":"20103","data":null,"msg":"手机号不能为空"}'
# data2 = json.loads(data1)
# print(data2)

# data3 = {'status': False, 'code': '20103', 'data': None, 'msg': '手机号不能为空'}
# data4 = json.dumps(data3)
# print(data4)
