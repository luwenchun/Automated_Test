"""
============================
Author:柠檬班-木森
Time:2020/1/3   17:12
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
一、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
 要求一：去除列表中的重复元素，
 要求二：删除 77，88，99这三个元素

二、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给打九折， 
如果购买金额大于100元会给打八折。编写一程序，询问购买价格，再打印出折扣和最终价格。 


三、输入一个5位整数（不需要考虑其他数据类型），判断它个位与万位相同，十位与千位相同。 
根据判断打印出相关信息，相同打印结果：该数据符合规范，不相同打印：该数据不符合规范
12321

四、利用random函数生成随机整数（范围1-9），然后用户输入一个数字，来进行比较：
如果大于随机数，则打印印大于随机数。
如果小于随机数，则打印小于随机数。
如果相等随机数，则打印等于随机数。

五、实现剪刀石头布游戏，运行代码，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）
电脑随机生成出拳数字，
然后比较胜负，打印游戏结果，

分析：
胜：
1    2     # 用户 减  电脑  = -1
2    3     # 用户 减  电脑  = -1
3    1     # 用户 减  电脑  = 2
if (user==1 and r ==2) or (user==2 and r ==3) or (user==3 and r ==1) :

if (user-r ==2) or (user -r==-1)：
    # 胜利
elif user==r:
    # 平局
else:
    # 输

输：
平：user == random




六、输入一个数，判断一个数n能同时被3和5整除，
能整除打印 :这个数据我喜欢 
不能整除打印：这个数据不太喜欢


七、总结笔记

"""
# 第1题：
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
# 去重
li = list(set(li))

# 删除77 88 99
li.remove(77)
li.remove(88)
li.remove(99)

# 第一题
money = float(input('请输入购买金额:'))
if money <= 0:
    print("输入有误")
elif 0 < money < 50:
    print('没有折扣，您需要支付{}元'.format(money))
elif 50 <= money <= 100:
    print('折扣为9折，您需要支付{}元'.format(money * 0.9))
else:
    print('折扣为8折，您需要支付{}元'.format(money * 0.8))

# 第二题
num_str = input('请输入五位数字:')
if num_str[0] == num_str[-1] and num_str[1] == num_str[-2]:
    print('此数字符合规范:{}'.format(num_str))
else:
    print('此数字不符合规范')

# 第三题
import random

n = random.randint(1, 9)
my_num = int(input('请输入数字:'))
if n < my_num:
    print('大于随机数')
elif n == my_num:
    print('等于随机数')
else:
    print('小于随机数')

# 第五题
import random

print('---石头剪刀布游戏开始----')
print('请按下面提示出拳：石头【1】 剪刀【2】 布【3】')
user_num = int(input('请输入你的选项：'))
# 电脑随机生成数字
r_num = random.randint(1, 3)
if 1 <= user_num <= 3:
    # 判断用户和电脑是否相等
    if r_num == user_num:
        print('您的出拳为:{}，电脑出拳:{}，平局'.format(user_num, r_num))
    # 判断用户胜利的情况
    elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
        print('您的出拳为:{}，电脑出拳:{}，您胜利了'.format(user_num, r_num))
    else:
        print('您的出拳为:{}，电脑出拳:{}，您输了'.format(user_num, r_num))
else:
    print('您出拳有误，请按规矩出拳')

# 第六题e
num = int(input("请输入数字"))
if num % 3 == 0 and num % 5 == 0:
    print("这个数字我喜欢")
else:
    print("这个数字不太喜欢")
