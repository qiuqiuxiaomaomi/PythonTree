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
    print client.topics
    topic = client.topics['bonaparte']

    balanced_consumer = topic.get_balanced_consumer(
        consumer_group="bonaparte",
        auto_commit_enable=True,
        zookeeper_connect='127.0.0.1:2181'
    )

    for message in balanced_consumer:
        print message.value