# -*- coding: UTF-8 -*-
'''
Created on 2020/4/1
@File  : test_get_ner.py
@author: ZL
@Desc  :妇科NER测试
'''

from api.get_ner import GetNer
import pytest
import allure


class TestNer(object):

    @pytest.mark.apitest
    @allure.feature("Ner实体识别")
    def test_get_ner(self):
        GetNer.get_ner(self, "bio_char.txt", "bio_char_result.csv", "ner_test_result.csv", "tag.txt")

