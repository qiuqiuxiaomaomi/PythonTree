#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pykafka import KafkaClient
import simplejson as json
import logging
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
logging.basicConfig()

if __name__ == '__main__':
    client=KafkaClient(hosts="127.0.0.1:9092")
    topic = client.topics['bonaparte']
    producer = topic.get_producer()
    producer.start()

    msg_dict = {
        "sleep_time": 10,
        "db_config": {
        "database":"",
        "host":"127.0.0.1",
        "user":"",
        "password":""
        },
        "table":"20180802temp",
        "msg":"bonaparte"
    }

    msg = json.dumps(msg_dict)
    producer.produce(msg)
    print msg
    producer.stop()