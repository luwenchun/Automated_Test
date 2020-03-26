"""
============================
Author:柠檬班-木森
Time:2020/3/9   21:38
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

from suds import client
import suds


class WebRequest:
    @staticmethod
    def send(url, method, *args, **kwargs):
        # 创建客户端对象
        cli = client.Client(url=url)
        # 根据参数构造请求方法
        request_method = eval('cli.service.{}'.format(method))
        try:
            # 发送请求
            res = request_method(*args, **kwargs)
        except suds.WebFault as e:
            # 提取请求错误信息返回
            return dict(e.fault)
        else:
            # 返回正常的信息
            return dict(res)


web = WebRequest()

res = web.send("http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl",
               "getCountryCityByIp",
               "125.1.1.44")
