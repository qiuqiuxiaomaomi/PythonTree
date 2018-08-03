#coding=utf-8

import requests
import json

class requeststest():
    def requestpost(self):
        data = {"a": 1, "b": 2}
        headers={}
        url_data = requests.post("http:\\www.baidu.com",
                                 data,
                                 headers)
        data_json = json.loads(url_data.text)
        if data_json['code'] == 0:
            print "请求成功"
        else:
            print "请求失败"

    def requestget(self):
        data = {"a": 1, "b": 2}
        headers = {}
        url_data = requests.get("http:\\www.baidu.com",
                                data,
                                headers)
        data_json = json.loads(url_data.text)
        if data_json['code'] == 0:
            print "请求成功"
        else:
            print "请求失败"