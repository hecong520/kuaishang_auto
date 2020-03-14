# -*- coding: UTF-8 -*-
'''
Created on 2020/2/26
@File  : test_get_similarity.py
@author: ZL
@Desc  :
'''

import os
import requests
import time
from common.change_data_type import ChangeDataType
from common.common_function import CommonFunction
from common.get_logging import Logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class GetSimilarity:

    def get_similarity(self, test_data_file, result_file):
        # self.logging = Logging()
        test_data = ChangeDataType.csv_to_dict(rootPath + "\\testdata\\apidata\\" + test_data_file)
        score_list = []
        re_score_list = []
        tf_list = []
        re_score = ""
        tf = ""
        for idx, temp in test_data.iterrows():
            label = int(temp["label"])
            str1 = temp["症状a"]
            str2 = temp["症状b"]
            url = "http://192.168.1.74:8999/symptom_similarity/v1?symptom1={}&symptom2={}".format(str1, str2)
            try:
                r = requests.get(url, timeout=50)
                result = r.json()
                score = result["data"]["score"]
                re_score = CommonFunction.get_re_score(score, 0.5)
                tf = CommonFunction.get_tf(re_score, label)
            except Exception as e:
                score = "bad request"
                print(score)
            # self.logging.info("症状1：" + str1 + "---症状2：" + str2 + "---预期分数："
            #                   + str(label) + "---实际分数：" + str(re_score) + "---是否一致：" + tf)
            score_list.append(score)
            re_score_list.append(re_score)
            tf_list.append(tf)
        test_data["score"] = score_list
        test_data["re_score"] = re_score_list
        test_data = CommonFunction.get_collections(test_data, tf_list)
        now = time.strftime('%y_%m_%d-%H_%M_%S')
        test_data.to_excel(rootPath + '\\testresults\\resultfile\\' + now + result_file, index=False,
                           encoding="utf-8")
