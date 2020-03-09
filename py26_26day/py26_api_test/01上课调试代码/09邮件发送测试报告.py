"""
============================
Author:柠檬班-木森
Time:2020/3/4   21:32
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import smtplib
from email.mime.text import MIMEText

"""
smtp服务器：
smtp服务器地址：
qq邮箱：smtp.qq.com   端口：465
163邮箱：smtp.163.com  端口：465

账号：musen_nmb@qq.com
授权码：algmmzptupjccbab


"""

# 第一步：连接邮箱的smtp服务器，并登录
smtp = smtplib.SMTP_SSL(host="smtp.qq.com", port=465)
smtp.login(user="musen_nmb@qq.com", password="algmmzptupjccbab")

# 第二步：构建一封邮件
with open("report1.html", "r", encoding="utf8") as f:
    content = f.read()

msg = MIMEText(content, _subtype="html", _charset="utf8")
# 主题
msg["Subject"] = "26期上课发送邮件"
# 发件人
msg["From"] = "musen_nmb@qq.com"
# 收件人
msg["To"] = "musen@qq.com"

# 第三步：发送邮箱
smtp.send_message(msg, from_addr="musen_nmb@qq.com", to_addrs=["3247119728@qq.com",])
