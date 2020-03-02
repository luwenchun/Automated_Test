# 一、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
#  要求一：去除列表中的重复元素，
#  要求二：去重后删除 77，88，99这三个元素
# li = [11,22,33,22,22,44,55,77,88,99,11]
# distinct = set(li)
# print(distinct)
#
# aa = list(distinct)
# aa.sort()
# bb = aa[0:-3]
# print(bb)

# 二、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给打九折，
# 如果购买金额大于100元会给打八折。编写一程序，询问购买价格，再打印出折扣和最终价格。

# price=float(input('请输入产品价格：'))
# if 50 <= price <= 100:
#     print('折扣为9折,最终价格为：{:.2f}元'.format(price*0.9))
# elif price > 100:
#     print('折扣为8折,最终价格为：{:.2f}元'.format(price*0.8))
# else:
#     print('非常抱歉，此次活动消费大于50元才可以打折')

#  三、输入一个5位整数（不需要考虑其他数据类型），判断它个位与万位相同，十位与千位相同。
# 根据判断打印出相关信息，相同打印结果：该数据符合规范，不相同打印：该数据不符合规范
#
# num = input('请输入一个5位整数:')
#
# if num[::1] == num[::-1]:
#     print('该数据符合规范')
# else:
#     print('该数据不符合规范')


#
# 四、利用random函数生成随机整数（范围1-9），然后用户输入一个数字，来进行比较：
# 如果大于随机数，则打印印大于随机数。
# 如果小于随机数，则打印小于随机数。
# 如果相等随机数，则打印等于随机数。

# import random
# num_1 = random.randint(1,9)
# print('随机数为:{}'.format(num_1))
#
# num_2 = float(input('请输入你的数字:'))
# if num_2 > num_1:
#     print('大于随机数')
# elif num_2 < num_1:
#     print('小于随机数')
# else:
#     print('等于随机数')
#
# 五、实现剪刀石头布游戏，运行代码，提示用户输入出拳的数字 ：石头（1）／剪刀（2）／布（3）
# 电脑随机生成出拳数字，
# 然后比较胜负，打印游戏结果，
# import random
# computer_quan = random.randint(1,3)
# print('电脑出拳为:{}'.format(computer_quan))
#
# user_quan = int(input("请输入您的出拳数字,石头（1）／剪刀（2）／布（3）:"))
# if computer_quan == user_quan:
#     print('平局')
#
# elif user_quan - computer_quan == -1 or user_quan - computer_quan == 2:
#     print('用户赢得比赛')
#
# elif user_quan - computer_quan == 1 or user_quan - computer_quan == -2:
#     print('用户输了')
#
# else:
#     print("出拳错误，请重新输入。规则如下:石头（1）／剪刀（2）／布（3）")

# 六、提示用户输入一个数（只考虑整数），判断这个数能同时被3和5整除，
# 能整除打印 :这个数据我喜欢
# 不能整除打印：这个数据不太喜欢
# num = int(input('请输入一个数:'))
# if num % 3 == 0 and num % 5 == 0:
#     print('这个数据我喜欢 ')
# else:
#     print('这个数据不太喜欢')



