"""
============================
Author:柠檬班-木森
Time:2020/2/21   21:35
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import random


def random_phone():
    phone = "136"
    n = random.randint(100000000,999999999)
    phone +=str(n)[1:]
    # for i in range(8):
    #     n = random.randint(1, 9)
    #     phone += str(n)

    return phone


res = random_phone()
print(res)

data = '{"mobile_phone":"#phone#","pwd":"12345678","type":1,"reg_name":"34254sdfs"}'


data = data.replace("#phone#",res)
print(data)

