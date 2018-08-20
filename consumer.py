import json
import sys
from kafka import KafkaConsumer
from pymongo import MongoClient
import os
import time
time.sleep(10)


client = MongoClient("mongodb://172.20.0.3:27017")
db = client.test


consumer = KafkaConsumer(str(sys.argv[1]), bootstrap_servers=["192.168.0.156:32000","192.168.0.156:32001"], group_id= str(sys.argv[1]) + "-monitor")
for message in consumer:
    tweet = json.loads(message.value.decode())
    print(tweet)
    result = db.tweets.insert_one(
        {
            "key_word": str(sys.argv[1]),
            "tweet": str(tweet)
        }
    )
    
