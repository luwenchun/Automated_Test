# 1、一、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）

# for x in range(1,10):
#     print()
#     for y in range(1,x+1):
#         print(y, '*', x ,'=' ,x * y,end=' ')


# 2、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
# lis = []
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1, 5):
#             print('这是第{}次打印'.format(a*b*c),a,b,c)
#             if a != b and c !=b and a !=c:
#                 lis.append(a*100 + 10*b +c)
# print(lis)
# lis_01=set(lis)
# print(lis_01)

# 3、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，然后再提示用户选择 ：
# 加【1】    减【2】    乘【3】      除【4】，根据不同的选择完成不同的计算 ，然后返回结果。

# print('----------计算器-----------')
# print('规则为:加【1】    减【2】    乘【3】    除【4】')
# while True:
#     num1 = input('请输入第一个数字:')
#     num2 = input('请输入第二个数字:')
#     method_num = input('请选择计算方法:')
#     if type(num1) != int or type(num2) != int or type(method_num) != int:
#         def calculate(num1,num2):
#
#                 if method_num == 1:
#                     return num1 + num2
#                 elif method_num == 2:
#                     return  num1 - num2
#                 elif method_num == 3:
#                     return num1 * num2
#                 elif method_num == 4:
#                     return num1 / num2
#                 else:
#                     return '您输入的方法有误，请重新输入'
#         result = calculate(num1,num2)
#         print('最终的结果为:',result)
#     else:
#         print('输入不符合规则，请重新输入')


# 1、运行程序，提示用户，输入用户名，输入密码，再次确认密码。
# ​
# 2、判读用户名有没有被注册过，如果用户名被注册过了，那么打印结果该用户名已经被注册。
# ​
# 3、用户名没有被注册过，则判断两次输入的密码是否一致，一致的话则注册成功，否则给出对应的提示。

# info=[{'user': '1', 'pwd1': '2', 'pwd2': '2'}]
# name = input('请输入用户名:')
# pwd1 = input('请输入密码:')
# pwd2 = input('请再次确认密码:')
# for item in info:
#     if item['user'] == name:
#
#         print('该用户名已经被注册')
#         break
#     elif item['user'] != name:
#         if pwd1 != pwd2:
#             print('两次输入的密码不一致')
#             break
# else:
#     print('注册成功')
#     info.append({"user": name, "pwd1": pwd1, "pwd2": pwd2})
# print('用户信息',info)




