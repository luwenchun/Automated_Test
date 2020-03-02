"""
============================
Author:柠檬班-木森
Time:2019/12/28
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
1、用户输入一个数值，请使用比较运算符确认用户输入的是否为偶数？是偶数输出True,不是输出False
（提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法将字符串转换为数值类型，再做判段）
2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，然后随机生成购买的斤数（5到10斤之间），最后计算出应该支付的金额！
3、使用random模块和字符串拼接的方法，随机生成一个130开头的手机号码。
4、现有字符串    str1 = "PHP is the best programming language in the world! "
      要求一：将给定字符串的PHP替换为Python      
      要求二：替换以后，将字符串以空格为分割点进行分割得到一个列表
5、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周X”（要求：使用上课学过的知识点来做） 


"""
import random

print('----------第1题----------------')
# 用户输入
num = input('请输入数字:')
# 转换成int
num = int(num)
# 条件预算符做比较，打印结果
print(num % 2 == 0)


print('----------第2题----------------')
# 第二题
# 输入价格
price = input('请输入价格：')
# 转换为浮点数
price = float(price)
# 生成斤数
num = random.randint(5, 10)
print('购买斤数：', num)
# 计算价格
res = price * num
print('支付金额：', res)


print('----------第3题----------------')

# 生成一个9位数
r = random.randint(100000000, 999999999)
print(r)
phone = "130" + str(r)[1:]
print(phone)

print('----------第4题----------------')
# 第一题
str1 = "PHP is the best programming language in the world! "
# 要求一
str2 = str1.replace('PHP', 'python')
print(str2)
# 要求二
li_str = str2.split(' ')
print(li_str)

print('----------第5题----------------')
# 第二题
li = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
num = int(input('请输入1-7:'))
index = num - 1
data = li[index]
print('今天是:{}'.format(data))