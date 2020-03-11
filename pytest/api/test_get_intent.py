# -*- coding: UTF-8 -*-
'''
Created on 2020/2/27
@File  : test_get_intent.py
@author: ZL
@Desc  :
'''

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from api.get_intent import GetIntent
import pytest
import allure

import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class TestIntent(object):

    @pytest.mark.apitest
    @allure.feature("意图识别")
    def test_get_similarity(self):
        GetIntent.get_intent(self, "test3.csv", "test2.xls")
