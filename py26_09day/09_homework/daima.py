# 第一题
# with open("01homework.txt", "r", encoding="utf8") as f:
#     datas = f.readlines()
#     print(datas)
# dict={}
# for i in range(0,len(datas)):
#     # print(i)
#     dict["data{}".format(i)] = datas[i][0:-1]
# print(dict)

# 第二题
with open("02homework.txt", "r", encoding="utf8") as f:
    datas = f.readlines()
    # print(datas)

list=[]
for i in range(0,len(datas)):

    str = datas[i][0:-1].split(',')
    dict = {}
    for k in range(0,len(str)):
        print(str[k].split(':'))
        if k == 0:
            dict['url']=str[k].split(':')[1]

        elif k == 1:
            dict['mobilephone'] = str[k].split(':')[1]
        else:
            dict['pwd'] = str[k].split(':')[1]
    list.append(dict)
print(list)

# 第四题：扩展题（不要求提交，有时间的同学可以去思考一下）：
# 之前作业写了一个注册的功能，再之前的功能上进行升级，
# 要求：把所有注册成功的用户数据放到文件中进行保存，确保下一次运行代码的时候，上一次运行注册的账号数据还在。
#
#
#
# users = [{"name": "py01", "pwd": "123"},
#          {"name": "py02", "pwd": "123"},
#          {"name": "py03", "pwd": "123"},
#          {"name": "py04", "pwd": "123"}]
#
# def register():
#     # 注册功能
#     username = input('请输入新账号:')  # 输入账号
#     password1 = input('请输入密码：')  # 输入密码
#     password2 = input('请再次确认密码：')  # 再次确认密码
#
#     for user in users:  # 遍历出所有账号，判断账号是否存在
#         if username == user['name']:
#             print('该账户已存在')  # 账号存在，
#             break
#     else:
#         # 判断两次密码是否一致
#         if password1 != password2:
#             print('注册失败，两次输入的密码不一致')
#         else:
#             # 账号不存在 密码一样，则添加到账户列表中
#             users.append({'name': username, 'pwd': password2})
#             print('注册成功！')
#
#     with open('123.txt','a',encoding='utf-8') as f :
#         for item in users:
#             content1 = f.write(item['name'])
#             content2 = f.write(item['pwd'])
#
# register()
