# -*- coding: UTF-8 -*-
'''
Created on 2020/2/27
@File  : common_function.py
@author: ZL
@Desc  :
'''


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
