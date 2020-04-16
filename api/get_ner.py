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

    def get_ner_result(self, target_file, exp_bio_list, re_bio_list):
        """
        通过获取target列表，以及人工及接口返回的bio值，来计算每个target及平均的准确率，召回率，F1
        :param target_file: 储存target的文件
        :param data_file: 储存接口结果数据的文件
        """
        # 获取target列表
        target_list = CommonFunction.get_target(self, target_file)
        # 获取人工预期及接口返回的bio值list
        # exp_bio_list, re_bio_list = ChangeDataType.ner_csv_to_dict(
        #     rootPath + "\\testresults\\resultfile\\" + data_file)
        # 返回每个target的准确率，召回率，F1
        MultiClassByWord.multi_each_target(self, target_list, exp_bio_list,
                                           re_bio_list)
        # 返回平均的准确率，召回率，F1
        MultiClassByWord.multi_ave_target(self, exp_bio_list, re_bio_list, "0")

    def get_ner(self, origin_test_data_file, test_data_file, result_file, target_file):
        """
        通过target列表，以及人工及接口返回的bio
        :param origin_test_data_file: 原始的只有单个字及人工bio值的文件
        :param test_data_file: 转化成csv的原始数据文件
        :param result_file: 接口运行后，生成的接口结果文件
        :param target_file: 储存target的文件
        """
        # 调用get_txt_to_csv函数，将txt文件转换为csv文件
        CommonFunction.get_txt_to_csv(origin_test_data_file, test_data_file)
        # 调用get_ner_to_words函数，返回字列表，句子列表，及人工预期bio列表
        word_list, words_list, bios_list = CommonFunction.get_ner_to_words(test_data_file)
        result_bio_list = []
        tf_list = []
        # 创建或打开result_file文件
        f = open(rootPath + "\\testresults\\resultfile\\" + result_file, 'w+', encoding='utf-8',
                 newline="")
        csv_writer = csv.writer(f)
        # 输入csv文件四个列的title
        csv_writer.writerow(["word", "exp_bio", "re_bio", "tf"])
        # 计数，用于遍历word_list及bios_list对应的值
        n = -1
        for temp in words_list:
            # 请求接口，循环words_list中的每句话
            url = "http://192.168.1.74:8064/ner/v1?utterance={}&model_name=gynaecology".format(
                temp)
            try:
                r = requests.get(url, timeout=50)
                result = r.json()
                # 获取接口返回的data中的bio值
                re_bio = result["data"]["bio"]
                # 循环取接口返回的bio值
                for i in range(0, len(re_bio)):
                    n = n + 1
                    # 调用函数，查看人工bio与接口返回bio是否一致
                    tf = CommonFunction.get_tf(bios_list[n], re_bio[i])
                    # csv循环填入字，人工bio值，接口返回bio值，以及tf值
                    csv_writer.writerow([word_list[n], bios_list[n], re_bio[i], tf])
                    result_bio_list.append(re_bio[i])
                    tf_list.append(tf)
            except Exception as e:
                re_bio = "bad request"
        f.close()
        print("总数：", len(tf_list), "，一致数：", tf_list.count("TRUE"), "，不一致数：", tf_list.count("FALSE"), "，一致率：",
              "{:.2f}%".format(tf_list.count("TRUE") / len(tf_list) * 100), "，不一致率：",
              "{:.2f}%".format(tf_list.count("FALSE") / len(tf_list) * 100))
        # 调用函数，输出每个target及平均的准确率，召回率，F1
        GetNer.get_ner_result(self, target_file, bios_list, result_bio_list)
