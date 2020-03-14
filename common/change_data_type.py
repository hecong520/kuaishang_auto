# -*- coding: UTF-8 -*-
'''
Created on 2020/2/26
@File  : change_data_type.py
@author: ZL
@Desc  :
'''

import json
import pandas


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
        return test_data

