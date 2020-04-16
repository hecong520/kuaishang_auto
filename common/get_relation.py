# -*- coding: UTF-8 -*-
'''
Created on 2020/4/10
@File  : get_relation.py
@author: ZL
@Desc  : 完成两个文件（一个为question，一个为answer）之间的问答关系：可总结为：symptom和item，symptom和check，symptom和cause的关系
'''
import xlwt
import os
import openpyxl
import re
import pandas
import re
import numpy as np
from common.change_data_type import ChangeDataType

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class GetRelation:

    def get_intent_target(self, file):
        """
        储存所有咨询类的的意图，做储备
        :param file:所有咨询类的意图列表
        :return intent_list:返回所有的咨询类的意图列表
        """
        target_list = []
        file = open(rootPath + "\\testdata\\pregnant\\" + file, encoding="UTF-8")
        for line in file.readlines():
            target_list.append(line.strip())
        return target_list

    def get_answer(self, file):
        """
       查看answer中的有效数据，sentence，ner_title,ner_context并做储备，后期做调用
       :param file:answer文件
       """
        sentence_list = []
        each_ner_content = []
        each_ner_title = []
        each_ner_t_list = []
        each_ner_c_list = []
        test_data = ChangeDataType.csv_to_dict(rootPath + "\\testdata\\pregnant\\" + file)
        for idx, temp in test_data.iterrows():
            # 获取句子，实体，实体类别，意图等
            sentence = temp["句子"]
            ner = temp["实体"]
            ner_type = temp["实体类别"]
            # 获取每个句子所有的实体类别：如果一个句子有多个实体类别，中间用$分割
            ner_type_l = ner_type.split("$")
            # 判断是否有多个实体类别
            if len(ner_type_l) >= 2:
                # 根据$拆分每个ner
                ner_l = ner.split("$")
                # 循环遍历拆分每个ner和内容
                for i in range(1, len(ner_l)):
                    each_ner = ner_l[i].split(":")
                    # 拼接 每个ner的类别和内容
                    if i == 1:
                        each_ner_title.append(str(each_ner[0]))
                        each_ner_content.append(str(each_ner[1]))
                    if i >= 2:
                        each_ner_title.append("," + str(each_ner[0]))
                        each_ner_content.append("," + str(each_ner[1]))
                    # 拼接sentence，each_ner_content，each_ner_title
                    sentence_list.append(sentence)
                    each_ner_c_list.append(each_ner_content)
                    each_ner_t_list.append(each_ner_title)
            # 只有单个实体
            else:
                # 拆分ner和内容
                each_ner = ner.split("$")[1].split(":")
                # 拼接 ner的类别和内容
                each_ner_title.append(str(each_ner[0]))
                each_ner_content.append(str(each_ner[1]))
                # 拼接sentence，each_ner_content，each_ner_title
                sentence_list.append(sentence)
                each_ner_c_list.append(each_ner_content)
                each_ner_t_list.append(each_ner_title)
            # 重置 each_ner_content，each_ner_title
            each_ner_content = []
            each_ner_title = []
        print(sentence_list)
        print(each_ner_c_list)
        print(each_ner_t_list)

        # 建立表格，先将这三个list结果记录文档；sentence_list，each_ner_c_list，each_ner_t_list
        workbook = xlwt.Workbook()
        # 设置sheet名字
        sheet1 = workbook.add_sheet('answer统计结果', cell_overwrite_ok=True)
        # 设置三列title
        sheet1.write(0, 0, "sentence")
        sheet1.write(0, 1, "ner")
        sheet1.write(0, 2, "ner_context")
        # 循环填写三列内容
        for i in range(0, len(sentence_list)):
            sheet1.write(i + 1, 0, sentence_list[i])
            sheet1.write(i + 1, 1, each_ner_c_list[i])
            sheet1.write(i + 1, 2, each_ner_t_list[i])
        # 保存表格
        workbook.save(rootPath + '\\testresults\\resultfile\\' + "answer_collection_result.xls")

        return sentence_list, each_ner_c_list, each_ner_t_list

    def get_question(self, file):
        """
        查看question中的有效数据，sentence，ner_title,ner_context,intent，并做储备，后期做调用
        :param file:question文件
        """
        sentence_list = []
        intent_list = []
        each_intent_list = []
        each_ner_content = []
        each_ner_title = []
        each_ner_t_list = []
        each_ner_c_list = []
        test_data = ChangeDataType.csv_to_dict(rootPath + "\\testdata\\pregnant\\" + file)
        for idx, temp in test_data.iterrows():
            # 获取句子，实体，实体类别，意图等
            sentence = temp["句子"]
            ner = temp["实体"]
            ner_type = temp["实体类别"]
            intent = temp["意图"]
            # 获取每个句子所有的实体类别：如果一个句子有多个实体类别，中间用$分割
            ner_type_l = ner_type.split("$")
            # 判断intent在target文件中，并且不等于无
            if intent in GetRelation.get_intent_target(self, "intent_target.txt") and ner_type != "无":
                # 判断是否有多个实体类别
                if len(ner_type_l) >= 2:
                    sentence_list.append(sentence)
                    # 拼接意图
                    each_intent_list.append(intent)
                    # 根据$拆分每个ner
                    ner_l = ner.split("$")
                    # 循环遍历拆分每个ner和内容
                    for i in range(1, len(ner_l)):
                        each_ner = ner_l[i].split(":")
                        # 拼接 每个ner的类别和内容
                        if i == 1:
                            each_ner_title.append(str(each_ner[0]))
                            each_ner_content.append(str(each_ner[1]))
                        if i >= 2:
                            each_ner_title.append("," + str(each_ner[0]))
                            each_ner_content.append("," + str(each_ner[1]))
                    intent_list.append(each_intent_list)
                    each_ner_c_list.append(each_ner_content)
                    each_ner_t_list.append(each_ner_title)
                # 只有单个实体
                else:
                    # ner_l = ner.split("$")
                    sentence_list.append(sentence)
                    # 拼接意图
                    each_intent_list.append(intent)
                    # 拆分ner和内容
                    each_ner = ner.split("$")[1].split(":")
                    # 拼接 ner的类别和内容
                    each_ner_title.append(str(each_ner[0]))
                    each_ner_content.append(str(each_ner[1]))
                    intent_list.append(each_intent_list)
                    each_ner_c_list.append(each_ner_content)
                    each_ner_t_list.append(each_ner_title)
            # 拼接sentence，each_intent_list，each_ner_content，each_ner_title

            # 重置each_ner_content，each_ner_title，each_intent_list
            each_ner_content = []
            each_ner_title = []
            each_intent_list = []

        print(sentence_list)
        print(each_ner_c_list)
        print(each_ner_t_list)
        print(intent_list)

        # 建立表格，先将这四个list结果记录文档；sentence_list，each_ner_c_list，each_ner_t_list，intent_list
        workbook = xlwt.Workbook()
        # 设置sheet名字
        sheet1 = workbook.add_sheet('question统计结果', cell_overwrite_ok=True)
        # 设置四列title
        sheet1.write(0, 0, "sentence")
        sheet1.write(0, 1, "ner")
        sheet1.write(0, 2, "ner_context")
        sheet1.write(0, 3, "intent")
        # 循环填写四列内容
        for i in range(0, len(sentence_list)):
            sheet1.write(i + 1, 0, sentence_list[i])
            sheet1.write(i + 1, 1, each_ner_c_list[i])
            sheet1.write(i + 1, 2, each_ner_t_list[i])
            sheet1.write(i + 1, 3, intent_list[i])
        # 保存表格
        workbook.save(rootPath + '\\testresults\\resultfile\\' + "question_collection_result.xls")
        return sentence_list, each_ner_c_list, each_ner_t_list, intent_list


def get_relation(self, question, answer, result_file):
    answer_sentence_list, answer_each_ner_c_list, answer_each_ner_t_list = GetRelation.get_answer("answer.csv")
    question_sentence_list, question_each_ner_c_list, question_each_ner_t_list, question_intent_list = GetRelation.get_answer(
        "question.csv")


test = GetRelation()
test.get_question("question.csv")
