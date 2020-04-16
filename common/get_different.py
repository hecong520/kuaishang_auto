# -*- coding: UTF-8 -*-
'''
Created on 2020/2/27
@File  : get_different.py
@author: ZL
@Desc  : 额外的函数，用语处理之前廖老师需要的查看两次标注文件不一致的地方
'''

import pandas
import os
from common.common_function import CommonFunction

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class GetDifferent:

    def get_diff(self, file1, file2, result_file):
        """
        读取两个文件的不同之处
        :param file1: 第一次的标注文件
        :param file2: 第二次的标注文件
        :param result_file: 输出不一致的地方
        """
        tf_list = []
        data1 = pandas.read_excel(rootPath + "\\testdata\\" + file1)
        data2 = pandas.read_excel(rootPath + "\\testdata\\" + file2)
        test_data = pandas.merge(data1, data2, on=['sentence'], how='outer')
        # 取两个意图标签列表
        for idx, temp in test_data.iterrows():
            str1 = temp["intent_x"]
            str2 = temp["intent_y"]
            try:
                # 确定两个意图标签是否一致
                tf = CommonFunction.get_tf(str1, str2)
            except Exception as e:
                score = "bad request"
            print(score)
        tf_list.append(tf)

        print(test_data)
        test_data = CommonFunction.get_collections(self, test_data, tf_list)
        # 输出excel
        test_data.to_excel(rootPath + "\\testresults\\" + result_file, index=False)


test = GetDifferent()
test.get_diff("test1", "test2", "result1")
