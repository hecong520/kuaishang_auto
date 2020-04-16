# -*- coding: UTF-8 -*-
'''
Created on 2020/2/26
@File  : test_get_symptom_similarity.py
@author: ZL
@Desc  :
'''

import pytest
from api.get_similarity import GetSymptomSimilarity
import allure


class TestSymptomSimilarity(object):

    @pytest.mark.apitest
    @allure.feature("测试环境症状相似度")
    def test_get_symptom_similarity(self):
        GetSymptomSimilarity.get_similarity(self, "症状相似度.csv", "similarity_test_result.xls")

