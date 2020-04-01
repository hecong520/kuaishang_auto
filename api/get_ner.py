# -*- coding: UTF-8 -*-
'''
Created on 2020/3/23
@File  : get_ner.py
@author: ZL
@Desc  :
'''

import os
import requests
import csv
from common.common_function import CommonFunction
from common.change_data_type import ChangeDataType
from algorithm.algorithm_func import MultiClassByWord

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class GetNer:
    # 得出BIO两个结果列
    def get_data_list(self, test_data_file):
        test_data = ChangeDataType.nor_csv_to_dict(rootPath + "\\testresults\\resultfile\\" + test_data_file)
        lb_list1 = []
        lb_list2 = []
        for idx, temp in test_data.iterrows():
            lb_list1.append(str(temp["exp_bio"]))
            lb_list2.append(str(temp["re_bio"]))
        return lb_list1, lb_list2

    # 得出标签值
    def get_target(self, file):
        target_list = []
        file = open(rootPath + "\\testdata\\apidata\\" + file, encoding="UTF-8")
        for line in file.readlines():
            target_list.append(line.strip())
        return target_list

    # 调用函数得出准确率，召回率，F1
    def get_ner_result(self, target_file, data_file):
        target_list = GetNer.get_target(self, target_file)
        lb_list1, lb_list2 = GetNer.get_data_list(self, data_file)
        MultiClassByWord.multi_word_target(self, target_list, lb_list1, lb_list2)

    def get_ner(self, origin_test_data_file, test_data_file, result_file, target_file):
        CommonFunction.get_txt_to_csv(origin_test_data_file, test_data_file)
        word_list, words_list, bios_list = CommonFunction.get_ner_to_words(test_data_file)
        result_bio_list = []
        tf_list = []
        f = open(rootPath + "\\testresults\\resultfile\\" + result_file, 'w+', encoding='utf-8', newline="")
        csv_writer = csv.writer(f)
        csv_writer.writerow(["word", "exp_bio", "re_bio", "tf"])
        n = -1
        for temp in words_list:
            url = "http://192.168.1.74:8064/ner/v1?utterance={}&model_name=gynaecology".format(temp)
            try:
                r = requests.get(url, timeout=50)
                result = r.json()
                re_bio = result["data"]["bio"]
                for i in range(0, len(re_bio)):
                    n = n + 1
                    tf = CommonFunction.get_tf(bios_list[n], re_bio[i])
                    csv_writer.writerow([word_list[n], bios_list[n], re_bio[i], tf])
                    result_bio_list.append(re_bio[i])
                    tf_list.append(tf)
            except Exception as e:
                re_bio = "bad request"
        f.close()
        print("总数：", len(tf_list), "，一致数：", tf_list.count("TRUE"), "，不一致数：", tf_list.count("FALSE"), "，一致率：",
              "{:.2f}%".format(tf_list.count("TRUE") / len(tf_list) * 100), "，不一致率：",
              "{:.2f}%".format(tf_list.count("FALSE") / len(tf_list) * 100))
        GetNer.get_ner_result(self, target_file, result_file)
