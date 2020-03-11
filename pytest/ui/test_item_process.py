# -*- coding: UTF-8 -*-
'''
Created on 2020/3/6
@File  : test_item_process.py
@author: ZL
@Desc  :
'''
import pytest
from ui.item_process import ItemProcess
from selenium import webdriver


class TestItemProcess(object):

    @pytest.mark.webtest
    def test_item_process(self):
        '''验证项目问诊流程'''
        chromedriver = "E:/chromedriver/chromedriver"
        self.driver = webdriver.Chrome(chromedriver)
        self.url = "http://192.168.1.17:8002/chat"
        ItemProcess.item_process(self, self.driver, self.url)
        self.driver.quit()
