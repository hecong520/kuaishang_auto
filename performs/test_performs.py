# -*- coding: UTF-8 -*-
'''
Created on 2020/3/2
@File  : test1.py
@author: ZL
@Desc  :
'''

from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    # """意图识别"""
    # @task(1)
    # def get_intent(self):
    #     sentence = "你们医院怎么样"
    #     self.client.get("/andrology_intent/v2?sentence={}".format(sentence))

    """相似度识别"""

    # @task(2)
    # def get_similary(self):
    #     sentence1 = "龟头刺痒"
    #     sentence2 = "龟头瘙痒"
    #     with self.client.get("/symptom_similarity/v1?symptom1={}&symptom2={}".format(sentence1, sentence2),
    #                          catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure('Failed!')

    """项目识别"""
    # @task(3)
    # def get_similary(self):
    #     sentence1 = "龟头刺痒"
    #     sentence2 = "龟头瘙痒"
    #     self.client.get("/symptom_similarity/v1?symptom1={}&symptom2={}".format(sentence1, sentence2))

    # """NER实体识别"""
    # @task(4)
    # def get_similary(self):
    #     sentence1 = "龟头刺痒"
    #     sentence2 = "龟头瘙痒"
    #     self.client.get("/symptom_similarity/v1?symptom1={}&symptom2={}".format(sentence1, sentence2))
    #

    """NER实体识别"""
    @task(4)
    def get_similary(self):
        sentence1 = "我有点担心会恶化怎么办"
        self.client.get("/emotion_question_analyse/v1?client_utterance={}".format(sentence1))


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 5000
