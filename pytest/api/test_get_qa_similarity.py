# -*- coding: UTF-8 -*-
'''
Created on 2020/4/13
@File  : test_get_qa_similarity.py
@author: ZL
@Desc  :
'''

import pytest
from api.get_similarity import GetSymptomSimilarity
import allure


class TestQASimilarity(object):

    @pytest.mark.apitest
    @allure.feature("测试环境症状相似度")
    def test_get_qa_similarity(self):
        pass
        # GetSimilarity.get_qa_similarity(self, "症状相似度.csv", "similarity_test_result.xls")
