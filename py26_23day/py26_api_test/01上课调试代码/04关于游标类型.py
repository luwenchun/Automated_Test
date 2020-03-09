"""
============================
Author:柠檬班-木森
Time:2020/2/24   20:py26_32day
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import pymysql

"""
主机：
port：3306
用户：future
密码：123456
"""

# 第一步：连接到数据库
conn = pymysql.connect(host="120.78.128.25",
                       port=3306,
                       user="future",
                       password="123456",
                       # 通过设置游标类型，可以控制查询出来的数据类型
                       cursorclass=pymysql.cursors.DictCursor,
                       charset="utf8")

# 第二步:创建一个游标对象
cur = conn.cursor()


# 第三步：执行sql语句
# sql = "SELECT id FROM futureloan.member WHERE mobile_phone=13367899876"
sql2 = "SELECT id FROM  futureloan.member LIMIT 10"
res = cur.execute(sql2)
# 返回的是查询到的数据条数
# print(res)

# 第四步：获取查询的数据
# fechone:获取一条数据(返回的查询集中的第一条数据，元组类型)
data = cur.fetchone()
print(data)






