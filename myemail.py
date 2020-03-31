#!/usr/bin/python3
#coding:utf-8
import smtplib
import traceback
#from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
import os


def sendMail_no_img(receivers, subject, mail_msg):
    if receivers == '':
        return False
    sender = "auto@qa.do-global.com"
    message = MIMEMultipart()
    text = MIMEText(mail_msg, 'html', 'utf-8')
    # message['From'] = Header("菜鸟教程", 'utf-8')
    # message['To'] = Header(receivers, 'utf-8')
    message['to'] = ','.join(receivers)
    # subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(text)

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件:%s"%subject)
        traceback.print_exc()
    except Exception as e:
        print("Error: 无法发送邮件:%s"%subject)
        traceback.print_exc()

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text