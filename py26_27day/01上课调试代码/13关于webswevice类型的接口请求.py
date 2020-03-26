"""
============================
Author:柠檬班-木森
Time:2020/3/9   21:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

from suds import client


# 创建一个连接客户端

cli = client.Client(url="http://ws.lemonban.com/sms-service-war-1.0/ws/smsFacade.ws?wsdl")

# print(cli)

# 发送验证码接口的参数
data = {"client_ip":"125.1.2.3","tmpl_id":"1","mobile":"1335678987"}

# 发送请求到服务器
try:
    res = cli.service.sendMCode(data)
except Exception as e:
    print(e.document)
    print(dict(e.fault))
    # raise e
else:
    print(dict(res))