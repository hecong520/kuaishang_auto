# -*- coding: UTF-8 -*-
'''
Created on 2020/2/29
@File  : get_config.py
@author: ZL
@Desc  :
'''

import os
import configparser

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(rootPath + "\\testdata\\config.txt", encoding='UTF-8')
        self.conf = {}

    def get_email(self):
        # Email
        self.conf['login_email'] = self.config.get("email", "login_email")
        self.conf['login_password'] = self.config.get("email", "login_password")
        self.conf['port'] = self.config.get("email", "port")
        self.conf['smtp'] = self.config.get("email", "smtp")
        self.conf['Recipient'] = self.config.get("email", "Recipient")
        self.conf['subject'] = self.config.get("email", "subject")
        self.conf['mailbody'] = self.config.get("email", "mailbody")
        return self.conf


class GetXpath:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(rootPath + "\\testdata\\uidata\\xpath.txt", encoding='UTF-8')
        self.conf = {}

    def get_xpth(self):
        # UI
        self.conf['chat_box'] = self.config.get("ui-process", "chat_box")
        self.conf['send_btn'] = self.config.get("ui-process", "send_btn")
        return self.conf


class GetSQL:
    def get_sql(self):
        # SQL
        pass
