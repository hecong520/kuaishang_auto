# -*- coding: UTF-8 -*-
'''
Created on 2020/2/29
@File  : send_email.py
@author: ZL
@Desc  :
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
from common.get_config import Config

'''发送邮件'''


class SendEmail:

    def send_email(self, file):
        """
        发送Email
        :param file: 发送email时带的附件
        """
        # 配置文件中提取email信息
        config = Config()
        c = config.get_email()
        smtp_email = c["smtp"]
        port = c["port"]
        login_email = c["login_email"]
        login_password = c["login_password"]
        subject = c["subject"]
        Recipient = c["Recipient"]
        mailbody = c["mailbody"]

        # 配置smtp，登录邮箱
        smtp = smtplib.SMTP_SSL(smtp_email, port)
        smtp.login(login_email, login_password)

        # 添加附件信息
        att = MIMEApplication(open(file, 'rb').read())
        att.add_header('Content-Disposition', 'attachment', filename="report.zip")

        # 配置邮件信息，发送人，收件人，邮件名，附件等
        msgRoot = MIMEMultipart('related')
        msgRoot['To'] = Recipient
        msgRoot['From'] = login_email
        msgRoot['Subject'] = Header(subject, 'gb2312')
        msg = MIMEText(mailbody, 'html', 'utf-8 ')
        msgRoot.attach(msg)
        msgRoot.attach(att)

        try:
            # 发送邮件
            smtp.sendmail(login_email, Recipient, msgRoot.as_string())
            print("发送成功")
        finally:
            smtp.close
