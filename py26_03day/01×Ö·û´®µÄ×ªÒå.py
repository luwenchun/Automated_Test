"""
============================
Author:柠檬班-木森
Time:2019/12/27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
\n：表示的是一个换行符  --->换行
\t:制表符   ----->  空格（tap键）
\\:  ---> \


r:防止转义


"""

s = "python\npython\t1234"
# print(s)

# 第一种方式
# s1 = "python\\npython\\t1234"
# print(s1)

# 第二种方法，在字符串前面使用r，防止字符串转义（定义的时候是什么样的，打印出来就是什么样的）
# s2 = r"python\npython\t1234"
# print(s2)

file_path = R"C:\apache-jmeter-5.2\backups"

print(file_path)