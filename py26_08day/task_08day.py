"""
============================
Author:柠檬班-木森
Time:2019/10/7
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


# 第一题
def mul_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{} * {} = {:<4}'.format(i,j,i*j),end="")
        print()

mul_table()


# for i in range(1, 10):
#     print()
#     for j in range(1, i + 1):
#         print('{}*{}={} '.format(i,j,i*j), end="")
# print()


# 第二题
def count_num():
    count = 0
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                if a != b and c != b and a != c:
                    print(a, b, c)
                    number = int('{}{}{}'.format(a,b,c))
                    print(number)
                    count += 1
    print('一共有{}个'.format(count))


count_num()


# 第三题

def compute_number():
    print('欢迎使用计算器')
    a = int(input('请输入数字1:'))
    b = int(input('请输入数字2:'))
    print('功能提示:【1】加 【2】减【3】乘 【4】除')
    num = input('请选择：')
    if num == '1':
        return a + b
    elif num == '2':
        return a - b
    elif num == '3':
        return a * b
    elif num == '4':
        return a / b
    else:
        print('没有此选项！')


res = compute_number()
print(res)
# 第四题

users = [{"name": "py01", "pwd": "123"},
         {"name": "py02", "pwd": "123"},
         {"name": "py03", "pwd": "123"},
         {"name": "py04", "pwd": "123"}]

def register():
    # 注册功能
    username = input('请输入新账号:')  # 输入账号
    password1 = input('请输入密码：')  # 输入密码
    password2 = input('请再次确认密码：')  # 再次确认密码

    for user in users:  # 遍历出所有账号，判断账号是否存在
        if username == user['name']:
            print('该账户已存在')  # 账号存在，
            break
    else:
        # 判断两次密码是否一致
        if password1 != password2:
            print('注册失败，两次输入的密码不一致')
        else:
            # 账号不存在 密码一样，则添加到账户列表中
            users.append({'name': username, 'pwd': password2})
            print('注册成功！')

register()
