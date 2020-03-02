"""
============================
Author:柠檬班-木森
Time:2020/2/12   19:33
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
配置文件类的封装

封装的目的：使用更简单


封装的需求：
    1、简化创建配置文件解析器对象，加载配置文件的流程（需要封装），提示（重写init方法）
    2、读取数据（不进行封装，使用原来的方法），通过继承父类即可
    3、简化写入数据的操作（需要封装），提示：自定义一个write_data方法。

"""


from configparser import ConfigParser

class HandleConfig(ConfigParser):

    def __init__(self, filename):
        # 调用父类的init方法
        super().__init__()
        self.filename = filename
        self.read(filename)

    def write_data(self, section, options, value):
        """写入数据的方法"""
        self.set(section, options, value)
        self.write(fp=open(self.filename, "w"))


# conf = ConfigParser()
# conf.read("conf.ini")

# conf.set("mysql","pwd","lemonban")
# conf.write(open("conf.ini","w"))

# conf2 = HandleConfig("conf.ini")
#
# # conf2.sections()
# host = conf2.get("mysql","host")
# print(host)
#
# conf2.write_data("mysql","user","python26")
