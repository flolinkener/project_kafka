import json
import sys
from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers=["192.168.0.21:32000","192.168.0.21:32001"])

i = 0 
j = 0
while i == 0:
    time.sleep(1)
    producer.send(str(sys.argv[1]), json.dumps(str(sys.argv[1])+ str(j)).encode())
    j += 1 

