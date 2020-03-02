"""
============================
Author:柠檬班-木森
Time:2020/2/14   20:09
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import os
import unittest
from py26_18day.py26_test_project.library.HTMLTestRunnerNew import HTMLTestRunner
from py26_18day.py26_test_project.common.handlepath import CASEDIR,REPORTDIR



# 第一步：创建套件
suite = unittest.TestSuite()


# 第二步：加载用例
loader = unittest.TestLoader()
# 通过路径进行加载
suite.addTest(loader.discover(CASEDIR))


# 第三步：执行用例

runner = HTMLTestRunner(stream=open(os.path.join(REPORTDIR,"report.html"),"wb"),
                        title="26期项目结构搭建生成的报告",
                        description="20200214写的代码",
                        tester="musen"
                        )
runner.run(suite)


