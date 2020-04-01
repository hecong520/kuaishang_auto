# -*- coding: UTF-8 -*-
'''
Created on 2020/2/26
@File  : test_get_similarity.py
@author: ZL
@Desc  :
'''

import pytest
from api.get_similarity import GetSimilarity
import allure


class TestSimilarity(object):

    @pytest.mark.apitest
    @allure.feature("症状相似度")
    def test_get_similarity(self):
        GetSimilarity.get_similarity(self, "症状相似度.csv", "similarity_test_result.xls")
