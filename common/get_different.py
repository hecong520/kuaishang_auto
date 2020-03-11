# -*- coding: UTF-8 -*-
'''
Created on 2020/2/27
@File  : get_different.py
@author: ZL
@Desc  :
'''

import pandas
import os
from common.common_function import Common_Function

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class Get_different():

    def get_diff(self, file1, file2, result_file):
        tf_list = []
        data1 = pandas.read_excel(rootPath + "\\testdata\\" + file1)
        data2 = pandas.read_excel(rootPath + "\\testdata\\" + file2)
        test_data = pandas.merge(data1, data2, on=['sentence'], how='outer')
        for idx, temp in test_data.iterrows():
            str1 = temp["intent_x"]
            str2 = temp["intent_y"]
            try:
                tf = Common_Function.get_tf(str1, str2)
            except Exception as e:
                score = "bad request"
            print(score)
        tf_list.append(tf)

        print(test_data)
        test_data = Common_Function.get_collections(self, test_data, tf_list)
        test_data.to_excel(rootPath + "\\testresults\\" + result_file, index=False)


test = Get_different()
test.get_diff("test1", "test2", "result1")
