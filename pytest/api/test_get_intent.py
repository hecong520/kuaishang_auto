# -*- coding: UTF-8 -*-
'''
Created on 2020/2/27
@File  : test_get_intent.py
@author: ZL
@Desc  :
'''

from api.get_intent import GetIntent
import pytest
import allure


class TestIntent(object):

    @pytest.mark.apitest
    @allure.feature("意图识别")
    def test_get_similarity(self):
        GetIntent.get_intent(self, "意图识别.csv", "test2.xls")
