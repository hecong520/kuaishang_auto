# -*- coding: UTF-8 -*-
'''
Created on 2020/2/26
@File  : test_get_symptom.py
@author: ZL
@Desc  : 症状归一化测试脚本，批量测试口语症状与李威整理的标准症状及詹威识别的标准症状，得出一致率
'''

from api.get_symptom import GetSymptom
import pytest
import allure


class TestSymptom(object):

    # @pytest.mark.sysmptiontest
    # @allure.feature("症状归一化")
    # def test_get_test_symptom(self):
    #     GetSymptom.get_symptom(self, "http://192.168.1.74:9001/symptom_norm/v1?symptoms={}", "口语-标准症状映射.json",
    #                            "symptom_test_result.xls")

    @pytest.mark.sysmptiontest
    @allure.feature("症状归一化")
    def test_get_pro_symptom(self):
        GetSymptom.get_pro_symptom(self, "http://10.13.8.230:8094/symptom_norm/v1?symptoms={}", "口语-标准症状映射.json",
                                   "symptom_pro_result.xls")
