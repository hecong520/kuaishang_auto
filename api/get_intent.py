# -*- coding: UTF-8 -*-
'''
Created on 2020/2/27
@File  : test_get_intent.py
@author: ZL
@Desc  :
'''

import os
import requests
import time
from common.change_data_type import ChangeDataType
from common.common_function import CommonFunction
from algorithm.algorithm_func import MultiClassByWord

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class GetIntent:

    def get_intent(self, test_data_file, result_file):
        test_data = ChangeDataType.csv_to_dict(rootPath + "\\testdata\\apidata\\" + test_data_file)
        score_list = []
        re_intent_list = []
        exp_intent_list = []
        tf_list = []
        for idx, temp in test_data.iterrows():
            intent = temp["intention"]
            sentence = temp["sentence"]
            url = "http://192.168.1.74:6688/andrology_intent/v2?sentence={}".format(sentence)
            try:
                r = requests.get(url, timeout=50)
                result = r.json()
                re_intent = result["data"]["intent"]
                score = result["data"]["score"]
                tf = CommonFunction.get_tf(intent, re_intent)
            except Exception as e:
                score = "bad request"
                print(e)
            # self.logging.info("句子：" + sentence + "---预期意图：" + intent
            #                   + "---实际意图：" + re_intent + "---是否一致：" + tf)
            score_list.append(score)
            exp_intent_list.append(intent)
            re_intent_list.append(re_intent)
            tf_list.append(tf)

        MultiClassByWord.multi_ave_target(self, exp_intent_list, re_intent_list)
        test_data["re_intent"] = re_intent_list
        test_data["score"] = score_list
        test_data = CommonFunction.get_collections(test_data, tf_list)
        now = time.strftime('%y_%m_%d-%H_%M_%S')
        test_data.to_excel(rootPath + '\\testresults\\resultfile\\' + now + result_file, index=False,
                           encoding="utf-8")
