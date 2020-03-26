"""
============================
Author:柠檬班-木森
Time:2020/2/26   21:13
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
re模块
findall:查找，并返回所有符合规则数据，返回一个列表

"""

import re

# findall方法使用
# s1 = "sdfghj13899998888fghjk13899998888lgh13899998888jk"
# res1 = re.findall("13899998788",s1)
# print(res1)

# 单字符
# \d:表示匹配一个数字
# s2 = "sdf   ghj13899998888f_gABSTSLhjk？#* ad [a\]"
# res1 = re.findall(r"\d",s2)
# print(res1)
# \D:表示匹配一个非数字
# res2 = re.findall(r"\D",s2)
# print(res2)

# \w:表示匹配一个单词字符（数字、字母、下划线）
res3 = re.findall(r"\w","")
print(res3)
# \W:表示匹配一个非单词字符（非数字、字母、下划线）
# res4 = re.findall(r"\W",s2)
# print(res4)

# \s:表示匹配一个空白（空格键，tap）
# res4 = re.findall(r"\s",s2)
# print(res4)

# \S:表示匹配一个非空白
# res4 = re.findall(r"\S",s2)
# print(res4)


# . 表示一个任意字符
# s2 = "abc123ABC?>* {)#&$"
# res5 = re.findall(r".",s2)
# print(res5)

# [],配置[]列举的字符
# s3 = "abc123ABC?>* {)#&$"
# res = re.findall(r"[12a?]",s3)
# print(res)

# 表示数量
# {N}:表示前面一个字符连续出现N次
# s4 = "sdfghj1389999888811111fghjk13829934788lgh13897889988jk135a34589111"
# res = re.findall(r"\d{11}", s4)
# print(res)

# {N,}:表示前面一个字符连续出现N次及以上
# s5 = "12345aaa56789aaaa4567890567890aaa456"
# res2 = re.findall(r"\d{4,}", s5)
# print(res2)

# {N,M}:表示前面一个字符出现N到M次

# s6 = "123456bbb123456b1234nn123b12345"
# res6 = re.findall(r"\d{3,5}", s6)
# print(res6)

# python中正则匹配的时候，默认是开启贪婪模式的。
# 关闭贪婪模式：？（表示数量，范围的后面加？就可以关闭贪婪模式）
# s6 = "123456bbb123456b1234nn123b12345"
# res6 = re.findall(r"\d{3,5}?", s6)
# print(res6)

# * :表示前面的这个字符出现任意次(包括0次)
# s7 = "1234abc123b"
# res7 = re.findall(r"\d*",s7)
# print(res7)

# + :表示前面的这个字符至少出现1次(包括1次)
# s7 = "1234abc123b"
# res7 = re.findall(r"\d+",s7)
# print(res7)

# ? :表示前一个字符出现0次或者一次
# s7 = "1234abc123b"
# res7 = re.findall(r"\d?",s7)
# print(res7)

# ?前是字符，则表示该字符出现0次或者1次，
# ？前是表示范围的，则是关闭贪婪模式  {n,}  {n,m}, + , *

# 表示边界
# ^ :表单字符串开头,$表单字符串结尾
# s = "python666java777php888python"
# res7= re.findall(r"thon$",s)
# print(res7)
# \b:表示单词边界   \B:表示非单词边界
# s = "python666 java777php?888python"
# res7= re.findall(r"\bjava",s)
# res7= re.findall(r"php\b",s)
# print(res7)
# res7= re.findall(r"python\B",s)
# print(res7)



# 需求配连续三个数字，或者连续aaa，或者hhh

# | 用来隔开多个匹配规则
# s1 = "121hhh678aaa"
# res = re.findall(r"\d{3}|aaa|hhh",s1)
# print(res)

# 表示分组
# (): 提取匹配规则中想要的数据
s3 = "12345#phone#67890987#pwd#6543244#member_id#4444"
res = re.findall(r"#(.+?)#",s3)
print(res)



# re.search()