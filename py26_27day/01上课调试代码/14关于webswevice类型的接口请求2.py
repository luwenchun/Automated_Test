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

cli = client.Client(url="http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl")

theIpAddress = "125.1.1.44"

res = cli.service.getCountryCityByIp(theIpAddress)

print(dict(res))
