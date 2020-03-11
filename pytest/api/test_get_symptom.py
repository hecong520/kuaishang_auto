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

    @pytest.mark.apitest
    @allure.feature("症状归一化")
    def test_get_symtom(self):
        GetSymptom.get_symtom(self, "test2.json", "test3.xls")

#
# if __name__ == '__main__':
#     unittest.main()
