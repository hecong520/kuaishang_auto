# -*- coding: UTF-8 -*-
'''
Created on 2020/3/13
@File  : take_roc.py
@author: ZL
@Desc  :
'''
import matplotlib.pyplot as plt


def get_data(path):
    f = open(path)
    data_list = f.readlines()
    return data_list


def get_truth_value():
    threshold_list = []
    truth_value = []
    data_list = get_data('test.txt')
    for item in data_list:
        truth_value.append(
            item.strip().split('\t')[2])

    return truth_value


def plot_curve(x, y):
    plt.scatter(x, y)
    plt.xlabel("假正例率", fontproperties='SimHei')
    plt.ylabel("真正例率", fontproperties='SimHei')
    plt.show()


def get_tpr_fpr():
    truth_value = get_truth_value()
    tpr = []
    fpr = []
    for i in range(1, len(truth_value)):
        forecast = []
        forecast.extend([1] * (i))
        forecast.extend([0] * (len(truth_value) - i))
        tmp_list = [forecast[j] * int(truth_value[j]) for j in range(len(forecast))]
        tp = sum(tmp_list[0:i])
        fp = i - tp
        fn = sum([int(x) for x in truth_value[i:len(truth_value)]])
        tn = len(truth_value) - i - fn
        print(tp, fp, fn, tn)
        tpr.append(tp * 1.0 / (tp + fn))
        fpr.append(fp * 1.0 / (tn + fp))

    return tpr, fpr


if __name__ == "__main__":
    x, y = get_tpr_fpr()
    plot_curve(y, x)
