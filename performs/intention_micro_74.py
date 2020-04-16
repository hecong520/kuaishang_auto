#!/user/bin/env  python
# -*- coding:utf-8 -*-

from locust import HttpLocust,task,TaskSet

class Userbehaviour(TaskSet):
    @task
    def Robot_inquiry(self):
        inqurystring = {
             "utterance": "我想咨询一下割双眼皮",
             "multi_intent_mode": False,
			 "enterprise":"beauty"

  }
        r = self.client.get("/intention/v1",params=inqurystring)
        result = r.json()
        assert r.status_code == 200
        assert result["code"] == 200


class WebSiteUser(HttpLocust):
    task_set = Userbehaviour
    host = "http://192.168.1.74:8198"
    min_wait = 1000
    max_wait = 2000



