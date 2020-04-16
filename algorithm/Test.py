# -*- coding: UTF-8 -*-
'''
Created on 2020/3/26
@File  : Test.py
@author: ZL
@Desc  :廖老师兴趣题：字符串全排列
'''
import itertools


class Test:
    def __init__(self):
        self.count = 0
        self.s_result = []

    def test1(self, str, i):
        s_begin = list(str)
        if i == len(s_begin):
            self.count = self.count + 1
            self.s_result.append(str)
        else:
            for j in range(i, len(s_begin)):
                s_begin[j], s_begin[i] = s_begin[i], s_begin[j]
                Test.test1(self, s_begin, i + 1)

        return self.s_result

    def test2(self, str):
        n = 0
        s_result = []
        s_begin = list(str)
        for x in itertools.permutations(s_begin, len(s_begin)):
            s_result.append(x)
            n = n + 1
        print(s_result)
        print(n)

    def test3(self):
        i = 6
        j = 6.0
        if i == j:
            result = "true"
        else:
            result = "false"
        print(result)


test = Test()
test.test3()
# test.test2("abcdef")
# print(test.test1("abcdef", 0))
