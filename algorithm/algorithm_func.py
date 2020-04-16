# -*- coding: UTF-8 -*-
'''
Created on 2020/3/13
@File  : algorithm_func.py
@author: ZL
@Desc  :
'''
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import recall_score, f1_score, precision_score, auc, confusion_matrix, classification_report, \
    accuracy_score
import numpy as np


class Binary:
    @staticmethod
    def get_auc(truth_value, prob_value):
        fpr, tpr, threshold = metrics.roc_curve(truth_value, prob_value)
        re_auc = auc(fpr, tpr)
        return re_auc, fpr, tpr

    @staticmethod
    def get_recall_score(truth_value, prob_value):
        recall = recall_score(truth_value, prob_value)
        return recall

    @staticmethod
    def get_f1_score(truth_value, prob_value):
        f1 = f1_score(truth_value, prob_value)
        return f1

    @staticmethod
    def get_precision_score(truth_value, prob_value):
        precision = precision_score(truth_value, prob_value)
        return precision

    @staticmethod
    def get_accuracy_score(truth_value, prob_value):
        accuracy = precision_score(truth_value, prob_value)
        return accuracy

    @staticmethod
    def binary_plot_curve(truth_value, prob_value):
        re_auc, fpr, tpr = Binary.get_auc(truth_value, prob_value)
        plt.plot(fpr, tpr, color='darkorange', lw=1, label='TEST ROC curve (area = %0.2f)' % re_auc)
        f1 = Binary.get_f1_score(truth_value, prob_value)
        recall = Binary.get_recall_score(truth_value, prob_value)
        precision = Binary.get_precision_score(truth_value, prob_value)
        Accuracy = Binary.get_accuracy_score(truth_value, prob_value)
        print("AUC值为：", re_auc)
        print("召回率R为：", recall)
        print("准确率P为：", precision)
        print("F1值为：", f1)
        print("Accuracy值为：", Accuracy)
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('TEST Example')
        plt.legend(loc="lower right")
        plt.show()


class MultiClassByWord:

    @staticmethod
    def get_classification_report(truth_value, prob_value):
        classify_report = classification_report(truth_value, prob_value)
        return classify_report

    @staticmethod
    def get_confusion_matrix(truth_value, prob_value):
        confusion_matrix_result = confusion_matrix(truth_value, prob_value)
        return confusion_matrix_result

    @staticmethod
    def get_overall_accuracy(truth_value, prob_value):
        overall_accuracy = accuracy_score(truth_value, prob_value)
        return overall_accuracy

    @staticmethod
    def get_precision_for_each_class(truth_value, prob_value):
        precision_for_each_class = precision_score(truth_value, prob_value, average='micro')
        return precision_for_each_class

    @staticmethod
    def get_average_accuracy(truth_value, prob_value):
        precision_for_each_class = MultiClassByWord.get_precision_for_each_class(truth_value, prob_value)
        average_accuracy = np.mean(precision_for_each_class)
        return average_accuracy

    @staticmethod
    def get_f1_score(truth_value, prob_value):
        f1 = f1_score(truth_value, prob_value, average=None)
        return f1

    @staticmethod
    def get_score(truth_value, prob_value):
        score = accuracy_score(truth_value, prob_value)
        return score

    @staticmethod
    def get_recall_score(truth_value, prob_value):
        recall = recall_score(truth_value, prob_value, average=None)
        return recall

    @staticmethod
    def get_precision_score(truth_value, prob_value):
        precision = precision_score(truth_value, prob_value, average=None)
        return precision

    @staticmethod
    def get_accuracy_score(truth_value, prob_value):
        accuracy = np.mean(precision_score(truth_value, prob_value, average=None))
        return accuracy

    def get_auc(truth_value, prob_value):
        fpr, tpr, threshold = metrics.roc_curve(truth_value, prob_value)
        re_auc = auc(fpr, tpr)
        return re_auc, fpr, tpr

    def get_recall_score1(tp, fn):
        r = tp / (tp + fn)
        return r

    def get_precision_score1(tp, fp):
        p = tp / (tp + fp)
        return p

    def get_f1_score1(tp, fp, fn):
        P = tp / (tp + fp)
        R = tp / (tp + fn)
        return 2 * P * R / (P + R)

    def get_each_class_target(self, lb_list1, lb_list2, point):
        tp, fp, fn, tn, n = MultiClassByWord.get_result_prob(self, lb_list1, lb_list2, point)
        recall = MultiClassByWord.get_recall_score1(tp, fn)
        precision = MultiClassByWord.get_precision_score1(tp, fp)
        f1 = MultiClassByWord.get_f1_score1(tp, fp, fn)
        return recall, precision, f1, n

    # 得出每个分类的tp, fp, fn, tn值
    def get_result_prob(self, lb_list1, lb_list2, point):
        n = 0
        fn = 0
        tp = 0
        fp = 0
        tn = 0
        for i in range(0, len(lb_list1)):
            n = n + 1
            if point in lb_list1[i]:
                if lb_list1[i] == lb_list2[i]:
                    tp = tp + 1
                elif point in lb_list2[i]:
                    fp = fp + 1
                    fn = fn + 1
                else:
                    fn = fn + 1
            elif point in lb_list2[i]:
                if lb_list1[i] != lb_list2[i]:
                    fp = fp + 1
            else:
                tn = tn + 1
        return tp, fp, fn, tn, n

    # 得出每个分类的tp, fp, fn, tn值
    def class_target(self, bz_intent_list, re_intent_list, point):
        pn = 0
        rn = 0
        tn = 0
        result = list(zip(bz_intent_list, re_intent_list))
        count_all_p = 0
        count_p = 0
        count_all_r = 0
        count_r = 0
        for res in result:
            bz_bio = res[0]  # 人工标注
            re_bio = res[1]  # 接口返回
            if bz_bio == point:
                count_all_r += 1
                pn = pn + 1
                if bz_bio == re_bio:
                    count_r += 1
                    tn = tn + 1
            if re_bio == point:
                rn = rn + 1
                count_all_p += 1
                if bz_bio == re_bio:
                    count_p += 1
        if count_all_p != 0 and count_all_r != 0:
            p = count_p / count_all_p
            r = count_r / count_all_r
            f1 = 2 * p * r / (p + r)
        else:
            p = 0
            r = 0
            f1 = 0
        return p, r, f1, pn, rn, tn

    # 直接算出平均召回率，准确率，F1值
    def ave_target(self, bz_intent_list, re_intent_list, point):
        pn = 0
        rn = 0
        tn = 0
        n = 0
        result = list(zip(bz_intent_list, re_intent_list))
        count_all_p = 0
        count_p = 0
        count_all_r = 0
        count_r = 0
        for res in result:
            bz_bio = res[0]  # 人工标注
            re_bio = res[1]  # 接口返回
            n = n + 1
            if bz_bio != point:
                count_all_r += 1
                pn = pn + 1
                if bz_bio == re_bio:
                    count_r += 1
                    tn = tn + 1
            if re_bio != point:
                count_all_p += 1
                rn = rn + 1
                if re_bio == bz_bio:
                    count_p += 1
        p = count_p / count_all_p
        r = count_r / count_all_r
        f1 = 2 * p * r / (p + r)
        return p, r, f1, pn, rn, tn

    def multi_each_target(self, target_list, bz_intent_list, re_intent_list):
        recall_list = []
        precision_list = []
        f1_list = []
        pn_list = []
        rn_list = []
        tn_list = []
        for i in range(0, len(target_list)):
            print("------", target_list[i], "------")
            p, r, f1, pn, rn, tn = MultiClassByWord.class_target(self, bz_intent_list, re_intent_list, target_list[i])
            print("人工标注数量为：", pn)
            print("接口预测数量为：", rn)
            print("结果一致数量为：", tn)
            print("准确率P为：", p)
            print("召回率R为：", r)
            print("F1为：", f1)
            recall_list.append(r)
            precision_list.append(p)
            f1_list.append(f1)
            pn_list.append(pn)
            rn_list.append(rn)
            tn_list.append(tn)
        return precision_list, recall_list, f1_list, pn_list, rn_list, tn_list

    def multi_ave_target(self, bz_intent_list, re_intent_list, point):
        print("------平均值(有效数据)------")
        p, r, f1, pn, rn, tn = MultiClassByWord.ave_target(self, bz_intent_list, re_intent_list, point)
        print("人工标注数量为：", pn)
        print("接口预测数量为：", rn)
        print("结果一致数量为：", tn)
        print("召回率R为：", r)
        print("准确率P为：", p)
        print("F1为：", f1)
        return p, r, f1, pn, rn, tn
