"""
============================
Author:柠檬班-木森
Time:2019/12/25
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
random.random()：生成0-1之间的随机数

random.randint()：在指定范围内，生成一个整数


查看官方库的源码：按住ctrl，鼠标点击即可进入源码


"""
import random

# 生成0-1之间的随机小数（）
# a = random.random()
# print(a)

# 在指定范围内，生成一个整数(包含范围的边界值)
# num = random.randint(1, 3)
# print(num)

# 如何生成指定范围内的小数
#  随机的整数+小数

number = random.randint(1, 4) + random.random()
print(number)