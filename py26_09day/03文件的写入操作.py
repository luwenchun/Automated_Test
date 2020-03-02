"""
============================
Author:柠檬班-木森
Time:2020/1/13   20:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
python操作文件

open的常用参数：

第一个：要打开的文件名字或者文件路径
第二个参数：文件打开的模式
    r:只读模式,如果打开的文件不存在，直接报错
    rb:只读模式，以二进制的编码格式去打开文件
    
    a: 以追加写入的模式打开文件，如果打开的文件不存在，不会报错（会自动创建一个）
    ab: 以追加写入的模式打开文件，如果打开的文件不存在，不会报错（会自动创建一个），二进制的编码格式去打开文件
   
    w: 以写入的模式打开文件，覆盖写入(会将原文件中的内容给清空），如果打开的文件不存在，不会报错（会自动创建一个）
    wb: 以写入的模式打开文件，覆盖写入(会将原文件中的内容给清空），如果打开的文件不存在，不会报错（会自动创建一个），二进制的编码格式去打开文件
     
    注意点：a,ab，w,wb，只能写入内容，不能读取内

第三个参数：
    encoding：用来指定打开文件的编码格式（使用rb的时候，不需要加该参数）




关于文件写入的方法：





"""
#  ---追加写入
# 打开文件
# f = open("tttt1111.txt","a",encoding="utf8")
# f.write("python26大佬很多")
# # 关闭文件
# f.close()

# ----覆盖写入
# 打开文件
# f = open("tttt1111.txt","w",encoding="utf8")
# f.write("python26")
# # 关闭文件
# f.close()


#  案例：以文件读写的方式，去复制一张图片

# 1、打开待复制的文件
f = open("bj2.png", "rb")
# 2、读取内容
content = f.read()
# 3、打开复制的新文件
f2 = open("bj2_copy1.png","wb")
# 4、写入读取出来的内容
f2.write(content)

# 5、关闭两个文件
f.close()
f2.close()





