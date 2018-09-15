#!/usr/bin/env python
# -*- coding:utf-8 -*-

from kazoo.client import KazooClient
from kazoo.recipe.lock import lock
import mysql.connector
import time
import logging
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
logging.basicConfig()

if __name__ == '__main__':
    zk_config = {
        "hosts": "127.0.0.1:20881, 127.0.0.1:20881, 127.0.0.1:20881",
        "timeout": 5000,
        "read_only": False
    }

    zk = KazooClient(zk_config)
    zk.start()
    lock = zk.Lock("/locksql", "lock_1")
    with lock:
        print "加锁"