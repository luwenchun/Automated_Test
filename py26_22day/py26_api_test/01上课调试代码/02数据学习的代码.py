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
                       charset="utf8")

# 第二步:创建一个游标对象
cur = conn.cursor()


# 第三步：执行sql语句
# sql = "SELECT id FROM futureloan.member WHERE mobile_phone=13367899876"
sql2 = "SELECT * FROM  futureloan.member LIMIT 10"
res = cur.execute(sql2)
# 返回的是查询到的数据条数
# print(res)

# 第四步：获取查询的数据
# fechone:获取一条数据(返回的查询集中的第一条数据，元组类型)
data = cur.fetchone()
print(data)
# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchone())


# 获取查询集中的所有数据
# datas = cur.fetchall()
# print(datas)


# 注意点：pymysql操作数据库。默认是开启事务的。
# 关键增加、删除、修改等相关涉及到数据库中数据变动的sql语句执行
# 执行的方式和查询是一样的
# cur.execute(sql2)
# 在执行完sql语句之后，要多出一步：调用commit提交事务
# conn.commit()




# pymssql  操作sql server
# cx_oracle: 操作oracel

