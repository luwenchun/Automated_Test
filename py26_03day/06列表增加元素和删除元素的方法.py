"""
============================
Author:柠檬班-木森
Time:2019/12/27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
添加元素的方法：
append:往列表尾部加入元素

insert:指定位置插入元素
# 第一个参数：插入数据的位置
# 第二个参数：插入的数据

extend:一次性在列表的尾部添加多个元素



删除元素的方法：

remove:删除指定的元素

pop：根据下标删除对应的元素

clear：清空列表

"""

li = [1, 2, 3]

# append方法：往列表尾部加入元素
# li.append(999)

# insert:指定位置插入元素
# 第一个参数：插入数据的位置
# 第二个参数：插入的数据
# li.insert(0, 66)

# extend:一次性在列表的尾部添加多个元素
# li.extend([11, 22, 33])


# 删除元素的方法
# remove：删除指定的元素(删除不存在的元素会报错)
# li.remove(2)

# pop：根据下标删除对应的元素(默认删除最后一个，也可以通过传参数来指定下标)
# li.pop(1)


# clear:清空列表
li.clear()



print(li)









