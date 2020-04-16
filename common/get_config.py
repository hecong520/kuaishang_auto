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
        """
        初始化config，读取config文件
        """
        self.config = configparser.ConfigParser()
        self.config.read(rootPath + "\\testdata\\config.txt", encoding='UTF-8')
        self.conf = {}

    def get_email(self):
        """
        获取email的各种参数配置值
        """
        self.conf['login_email'] = self.config.get("Email", "login_email")
        self.conf['login_password'] = self.config.get("Email", "login_password")
        self.conf['port'] = self.config.get("Email", "port")
        self.conf['smtp'] = self.config.get("Email", "smtp")
        self.conf['Recipient'] = self.config.get("Email", "Recipient")
        self.conf['subject'] = self.config.get("Email", "subject")
        self.conf['mailbody'] = self.config.get("Email", "mailbody")
        return self.conf


class GetXpath:
    def __init__(self):
        """
        初始化config，读取xpath文件
        """
        self.config = configparser.ConfigParser()
        self.config.read(rootPath + "\\testdata\\uidata\\xpath.txt", encoding='UTF-8')
        self.conf = {}

    def get_xpth(self):
        """
        获取xpath的各种参数配置值
        """
        self.conf['chat_box'] = self.config.get("UI-PROCESS", "chat_box")
        self.conf['send_btn'] = self.config.get("UI-PROCESS", "send_btn")
        return self.conf


class GetSQL:
    def get_sql(self):
        # SQL
        pass
