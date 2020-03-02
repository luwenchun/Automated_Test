# 1、实现一个文件复制器函数，通过给函数传入一个路径，复制该路径下面所有的文件(目录不用复制)到当前目录，
# 要求：如果传路径不存在，不能报错
# 提示：os模块结合文件读写操作 、异常捕获 即可实现

# import os
# def copy(url):
#     try:
#         res = os.listdir(url)
#         print('要复制的目录下有这些文件',res)
#     except:
#         print('你输入的路径不正确请重试')
#     else:
#         print('成功执行')
#         for name  in res:
#             # 待复制文件路径
#             file_path = os.path.join(url, name)
#             print('待复制的路径', file_path)
#             # 当前要存放路径
#             base_dir = os.path.dirname(__file__)
#             now_path = os.path.join(base_dir, name)
#             print('要存放的路径', now_path)
#             # 读取待复制文件内容
#             with open(file_path, "r", encoding="utf8")as f1:
#                 content = f1.read()
#             # 保持读取的文件内容
#             with open(now_path, "w", encoding="utf8")as f2:
#                  f2.write(content)
#     finally:
#         print('成功失败都执行')
#
# copy('/Users/apple/Documents/ningmeng/py26_10day/copy')

# # 2、改善上节课扩展作业的注册程序，打开文件的读取数据的时候，如果文件不存在会报错，请通过try-except来捕获这个错误，进行处理，让注册程序可以继续运行。
# def work3():
#     try:
#         # 读取文件中注册用户的数据
#         with open('users11.txt', 'r', encoding='utf8') as f:
#             # 读取内容,使用eval识别字符串中的列表
#             users = eval(f.read())
#
#     except:
#         print("文件不存在报错")
#     else:
#
#
#         # 注册功能代码（上次作业写的，不需要改动）
#         username = input('请输入新账号:')  # 输入账号
#         password1 = input('请输入密码：')  # 输入密码
#         password2 = input('请再次确认密码：')  # 再次确认密码
#
#         for user in users:  # 遍历出所有账号，判断账号是否存在
#             if username == user['name']:
#                 print('该账户已存在')  # 账号存在，
#                 break
#         else:
#             # 判断两次密码是否一致
#             if password1 != password2:
#                 print('注册失败，两次输入的密码不一致')
#             else:
#                 # 账号不存在 密码一样，则添加到账户列表中
#                 users.append({'name': username, 'pwd': password2})
#                 print('注册成功！')
#
#         # 程序运行结束后，将所有用户的数据写入文件
#         with open('users.txt', 'w', encoding='utf8') as f:
#             # 将列表转换为字符串,写入文件
#             f.write(str(users))
#
#
# work3()
#
# # 3、优化之前作业的石头剪刀布游戏，用户输入时，如果输入非数字会引发异常，请通过异常捕获来处理这个问题。
# print('---石头剪刀布游戏开始----')
# print('请按下面提示出拳：石头【1】 剪刀【2】 布【3】结束【4】')
# while True:
#     try:
#         user_num = int(input('请输入你的选项：'))
#
#     except:
#         print("输入错误请输入数字")
#     else:
#         # 电脑随机生成数字
#         import random
#         r_num = random.randint(1, 3)
#
#         if 1 <= user_num <= 4:
#         # 判断用户和电脑是否相等
#
#                 if r_num == user_num:
#                     print('您的出拳为:{}，电脑出拳:{}，平局'.format(user_num, r_num))
#                 # 判断用户胜利的情况
#                 elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
#                     print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(user_num, r_num))
#                 elif user_num == 4:
#                     print('结束')
#                     break
#                 else:
#                     print('您的出拳为:{}，电脑出拳:{}，您输了'.format(user_num, r_num))
#         else:
#             print('您出拳有误，请按规矩出拳')
import os
def copy(path):
    try:
        file = os.listdir(path)
        print('即将要复制的文件:',file)
    except:
        print('不要影响后续进程')
    else:
        for i in file:
            print(i)
        copy_path = os.path.join(path,i)
        print(copy_path)
        paste_path = os.path.dirname(__file__)
        print(paste_path)
        paste_path01=os.path.join(paste_path,i)
        with open(copy_path,'r',encoding='utf-8') as f1:
            content = f1.read()
            print(content)
        with open(paste_path01,'w',encoding='utf-8') as f2:
            f2.write(content)

copy('/Users/apple/Documents/ningmeng/py26_10day/happy')
