"""
============================
Author:柠檬班-木森
Time:2020/2/24   20:58
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

from decimal import Decimal

# t = 1.1
# t2 = 9.3
# print(t,type(t))
# # 浮点数进行相减，小数位数会出现精度问题
# print(t2-t)

# 错误用法
# d1 = Decimal(9.3)
# d2 = Decimal(1.1)
# print(d1 - d2)

# 正确的用法
d22 = Decimal("9.3")
d11 = Decimal("1.1")
print(d22 - d11)

res = 90 + d22
print(res, type(res))
