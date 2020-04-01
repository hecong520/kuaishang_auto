# -*- coding: UTF-8 -*-
'''
Created on 2020/3/6
@File  : item_process.py
@author: ZL
@Desc  :
'''

from common.get_config import GetXpath
import time
from selenium.webdriver.common.action_chains import ActionChains
from common.change_data_type import ChangeDataType
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class ItemProcess:
    def get_process_data(self, file):
        test_data = ChangeDataType.json_to_dict(rootPath + "\\testdata\\uidata\\" + file)
        # print(test_data)
        # # 遍历item_process.json文件中的项目与项目问诊内容
        # for key in test_data:
        #     print(key + ':' + str(test_data[key]))
        return test_data

    def item_process(self, driver, url):
        config = GetXpath()
        self.c = config.get_xpth()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(15)

        # test_data = ItemProcess().get_process_data("item_inquiry_process.json")
        # 遍历item_process.json文件中的项目与项目问诊内容
        # for key in test_data:
        #     print(key + ':' + str(test_data[key]))
        driver.find_element_by_xpath(self.c["chat_box"]).send_keys("你好\n")
        time.sleep(10)


test = ItemProcess()
test.get_process_data("item_inquiry_process.json")
