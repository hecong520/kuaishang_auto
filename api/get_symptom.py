# -*- coding: UTF-8 -*-
'''
Created on 2020/2/26
@File  : test_get_symptom.py
@author: ZL
@Desc  : 症状归一化测试脚本，批量测试口语症状与李威整理的标准症状及詹威识别的标准症状，得出一致率
'''

import os
import requests
import xlwt
from common.change_data_type import ChangeDataType
from common.common_function import CommonFunction
import time
from algorithm.algorithm_func import Binary

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class GetSymptom:

    def get_symtom(self, test_data_file, result_file):
        # self.logging = Logging()
        test_data = ChangeDataType.json_to_dict(rootPath + "\\testdata\\apidata\\" + test_data_file)
        key_list = list(test_data.keys())
        value_list = list(test_data.values())
        result_value_list = []
        tf_list = []
        tf = ""
        for key, value in test_data.items():
            url = "http://192.168.1.74:9001/symptom_norm/v1?symptoms={}".format(key)
            try:
                r = requests.get(url, timeout=50)
                result = r.json()
                result_value = result["norm_symptoms"]
                tf = CommonFunction.get_tf(result_value, value[0])
            except Exception as e:
                print(e)
            # self.logging.info("口语症状：" + key + "---预期标准症状：" + value[0] + "---实际标准症状："
            #                   + result_value + "---是否一致：" + tf)
            result_value_list.append(result_value)
            tf_list.append(tf)

        Binary.binary_plot_curve(value_list, result_value_list)
        now = time.strftime('%y_%m_%d-%H_%M_%S')
        workbook = xlwt.Workbook()
        sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
        sheet1.write(0, 0, "口语症状")
        sheet1.write(0, 1, "预期标准症状")
        sheet1.write(0, 2, "实际标准症状")
        sheet1.write(0, 3, "是否一致")
        sheet1.write(0, 4, "总数")
        sheet1.write(1, 4, len(key_list))
        sheet1.write(0, 5, "一致数")
        sheet1.write(1, 5, tf_list.count("TRUE"))
        sheet1.write(0, 6, "不一致数")
        sheet1.write(1, 6, tf_list.count("FALSE"))
        sheet1.write(0, 7, "一致率")
        sheet1.write(1, 7, "{:.2f}%".format(tf_list.count("TRUE") / len(key_list)) * 100)
        sheet1.write(0, 8, "不一致率")
        sheet1.write(1, 8, "{:.2f}%".format(tf_list.count("FALSE") / len(key_list)) * 100)
        print("总数：", len(tf_list), " 一致数：", tf_list.count("TRUE"), " 不一致数：", tf_list.count("FALSE"), " 一致率：",
              "{:.2f}%".format(tf_list.count("TRUE") / len(tf_list) * 100), " 不一致率：",
              "{:.2f}%".format(tf_list.count("FALSE") / len(tf_list) * 100))
        for i in range(0, len(key_list)):
            sheet1.write(i + 1, 0, key_list[i])
            sheet1.write(i + 1, 1, value_list[i])
            sheet1.write(i + 1, 2, result_value_list[i])
            sheet1.write(i + 1, 3, tf_list[i])
        workbook.save(rootPath + '\\testresults\\resultfile\\' + now + result_file)
