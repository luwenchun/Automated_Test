# 1、 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？

# start= 100
# sum_once = 0#计算每轮高度 : 下落 +反弹
# sum = 0 #总共高度
#
# for i in range(1,11):
#     sum_once = start + start/2
#     print('第{0}轮经过米'.format(i),sum_once)
#
#     start = start/2
#     print('此时小球高度{0}.米'.format(start))
#
#     sum = sum+sum_once
#     print('第{0}次总高度{1}米'.format(i,sum))


# 2、猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半  在加一个。到第10天早上想再吃时，见只剩下一个桃子了。
# 请通过一段通过代码来计算第一天摘了多少个桃子？

# t = 1
# print('第10天吃之前就剩1个桃子')
# for i in range(1, 10):
#     t = (t+1) * 2
#     print('第%s天吃之前还有%s个桃子' % (i, t))
# print('第1天共摘了%s个桃子' % t)


# 3、使用循环和条件语对剪刀石头布游戏进行升级，提示用户输入要出的拳 ：
# 石头（1）／剪刀（2）／布（3）/退出（4）
# 电脑随机出拳比较胜负，显示 用户胜、负还是平局，打印结果，一轮游戏完了之后，
# print('---石头剪刀布游戏开始----')
# print('请按下面提示出拳：石头【1】 剪刀【2】 布【3】结束【4】')
# while True:
#     user_num = int(input('请输入你的选项：'))
#     # 电脑随机生成数字
#     import random
#     r_num = random.randint(1, 3)
#
#     if 1 <= user_num <= 4:
#     # 判断用户和电脑是否相等
#
#             if r_num == user_num:
#                 print('您的出拳为:{}，电脑出拳:{}，平局'.format(user_num, r_num))
#             # 判断用户胜利的情况
#             elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
#                 print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(user_num, r_num))
#             elif user_num == 4:
#                 print('结束')
#                 break
#             else:
#                 print('您的出拳为:{}，电脑出拳:{}，您输了'.format(user_num, r_num))
#     else:
#         print('您出拳有误，请按规矩出拳')













