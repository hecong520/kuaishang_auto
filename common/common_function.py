# -*- coding: UTF-8 -*-
'''
Created on 2020/2/27
@File  : common_function.py
@author: ZL
@Desc  :
'''
import csv
import zipfile
import os
import pandas
import re

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]


class CommonFunction:

    @staticmethod
    def get_url(port, path):
        url = "http://192.168.1.74:8999" + port + path
        return url

    @staticmethod
    def get_re_score(num, mid):
        if float(num) <= mid:
            re_score = 0
        else:
            re_score = 1
        return re_score

    @staticmethod
    def get_tf(str1, str2):
        if str1 == str2:
            tf = "TRUE"
        else:
            tf = "FALSE"
        return tf

    @staticmethod
    def get_collections(data, tf_list):
        data["是否一致"] = tf_list
        data["总数"] = len(tf_list)
        data["一致数"] = tf_list.count("TRUE")
        data["不一致数"] = tf_list.count("FALSE")
        data["一致率"] = "{:.2f}%".format(tf_list.count("TRUE") / len(tf_list) * 100)
        data["不一致率"] = "{:.2f}%".format(tf_list.count("FALSE") / len(tf_list) * 100)
        print("总数：", len(tf_list), "，一致数：", tf_list.count("TRUE"), "，不一致数：", tf_list.count("FALSE"), "，一致率：",
              "{:.2f}%".format(tf_list.count("TRUE") / len(tf_list) * 100), "，不一致率：",
              "{:.2f}%".format(tf_list.count("FALSE") / len(tf_list) * 100))
        return data

    @staticmethod
    def zip_file(dir_path, zip_path):
        zip = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
        for root, dirnames, filenames in os.walk(dir_path):
            file_path = root.replace(dir_path, '')  # 去掉根路径，只对目标文件夹下的文件及文件夹进行压缩
            # 循环出一个个文件名
            for filename in filenames:
                zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
        zip.close()

    @staticmethod
    def change_space_to_comma(test_data_file):
        # 清空文件内容（仅当以 "r+"   "rb+"    "w"   "wb" "wb+"等以可写模式打开的文件才可以执行该功能）
        f1 = open((rootPath + "\\testdata\\apidata\\" + test_data_file), 'r+', encoding='UTF-8', errors='ignore')
        infos = f1.read()
        line_new = re.sub('		', ',', infos)  # 替换功能
        f1.seek(0)  # 清空文件
        f1.truncate()
        f1.write(line_new)  # 重写
        f1.close()

    @staticmethod
    def get_txt_to_csv(test_data_file, result_data_file):
        CommonFunction.change_space_to_comma(test_data_file)
        with open((rootPath + "\\testdata\\apidata\\" + result_data_file), 'w+', encoding='UTF-8',
                  newline='') as csvfile:
            spamwriter = csv.writer(csvfile, dialect='excel')
            with open((rootPath + "\\testdata\\apidata\\" + test_data_file), 'r', encoding='UTF-8',
                      errors='ignore') as filein:
                spamwriter.writerow("--")
                for line in filein:
                    if "," in line:
                        if ",," in line:
                            line_list = line.strip('\n').split(',,')
                            if line_list[0] == "":
                                line_list[0] = "，"
                        else:
                            line_list = line.strip('\n').split(',')
                        spamwriter.writerow(line_list)
                    else:
                        spamwriter.writerow("--")
                spamwriter.writerow("--")

    @staticmethod
    def get_ner_to_words(file):
        test_data = pandas.read_csv(rootPath + "\\testdata\\apidata\\" + file, encoding="utf-8")
        bio_list = []
        re_word_list = []
        word_list = []
        words_list = []
        words_l = []
        bios_list = []
        for idx, temp in test_data.iterrows():
            if temp[1] != "-":
                word = temp[0]
                exp_bio = temp[1]
                re_word_list.append(word)
                word_list.append(word)
                words = "".join(word_list)
                bio_list.append(exp_bio)
                words_l.append(words)
            else:
                words_list.append(words_l[len(words_l) - 1])
                for i in range(0, len(bio_list)):
                    bios_list.append(bio_list[i])
                words_l = []
                word_list = []
                bio_list = []
        return re_word_list, words_list, bios_list
