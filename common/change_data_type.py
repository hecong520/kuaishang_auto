# -*- coding: UTF-8 -*-
'''
Created on 2020/2/26
@File  : change_data_type.py
@author: ZL
@Desc  :
'''

import json
import csv
import pandas
from common.common_function import CommonFunction
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class ChangeDataType:

    @staticmethod
    def json_to_dict(path):
        with open(path, mode='r', encoding='utf-8') as f2:
            test_data = json.load(f2)
            return test_data

    @staticmethod
    def dict_to_jsonfile(dict_data, file_name):
        with open(file_name, 'w') as f:
            # 设置不转换成ascii  json字符串首缩进
            f.write(json.dumps(dict_data, ensure_ascii=False, indent=2))

    @staticmethod
    def dict_to_json(dict_data):
        str_json = json.dumps(dict_data)
        return str_json

    @staticmethod
    def csv_to_dict(file):
        test_data = pandas.read_csv(file, encoding="utf-8")
        exp_list = []
        re_list = []
        for idx, temp in test_data.iterrows():
            exp_list.append(temp["exp_bio"])
            re_list.append(temp["re_bio"])
        return exp_list, re_list

    @staticmethod
    def nor_csv_to_dict(file):
        test_data = pandas.read_csv(file, encoding="utf-8")
        return test_data

    @staticmethod
    def zip_data(file):
        test_data1, test_data2, unit_word_list = CommonFunction.get_ner_to_words(file)
        return_data = zip(test_data1, test_data2)
        return return_data
