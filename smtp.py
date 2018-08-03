#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '59*********@qq.com'
receivers = ['*********@******']

message = MIMEText('Python 邮件发送测试', 'plain', 'utf-8')
message['From'] = Header("bonaparte", 'utf-8')
message['To'] = Header("Tree", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['subject'] = Header(subject, 'utf-8')

try:
    smtp_server = 'smtp.qq.com'
    passwd = '******'
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(sender, passwd)
    server.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "邮件发送失败"

