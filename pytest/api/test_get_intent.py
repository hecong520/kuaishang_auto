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

    @pytest.mark.eyeintenttest
    @allure.feature("意图识别")
    def test_get_eye_intent(self):
        # GetIntent.get_intent(self, "intent_tag.txt", "意图识别.csv", "intent_test_result.xls")
        GetIntent.get_eye_intent(self,
                                 "http://10.13.8.230:8062/intention/v1?utterance={}&multi_intent_mode=False&enterprise=ophthalmology",
                                 "eye_intent.csv",
                                 "ophthalmology_intention_to_test_7000.csv",
                                 "eye_intent_test_result.xls")

    # @pytest.mark.intenttest
    # @allure.feature("意图识别")
    # def test_get_test_intent(self):
    #     # GetIntent.get_intent(self, "intent_tag.txt", "意图识别.csv", "intent_test_result.xls")
    #     GetIntent.get_intent(self, "192.168.1.74:9008/check/vote/intention?sentence={}", "intent_tag.txt",
    #                          "意图识别.csv",
    #                          "intent_test_result.xls")
    #
    # @pytest.mark.intenttest
    # @allure.feature("意图识别")
    # def test_get_pro_intent(self):
    #     # GetIntent.get_intent(self, "intent_tag.txt", "意图识别.csv", "intent_test_result.xls")
    #     GetIntent.get_intent(self, "http://10.13.8.230:8098/andrology_intent/v2?sentence={}", "intent_tag.txt",
    #                              "意图识别.csv",
    #                              "intent_pro_result.xls")
