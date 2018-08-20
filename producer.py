from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sys
from kafka import KafkaProducer
import time
time.sleep(10)

producer = KafkaProducer(bootstrap_servers=["192.168.0.156:32000","192.168.0.156:32001"])

#Variables that contains the user credentials to access Twitter API 
access_token = "1021668963409973248-HTG0zto0i4yciDshtYuTMMKG7NSqoj"
access_token_secret = "0WV5duDxcxp4j2GW5tmoKAqt1FbOlJ9P0RUC08rgVuqVy"
consumer_key = "xHY7c5kD03rvtv3azkzAKxkrT"
consumer_secret = "jr2Yo8KtkGQ4ztp2qmAfAajoytfzYPl6Qh0NDpeW9gGtr8tRx6"

class Listener(StreamListener):
    

    def on_data(self, data):
        #print(data)
        producer.send(str(sys.argv[1]), json.dumps(data).encode())


    def on_error(self, status):
       print(status)

listener = Listener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener)
twitterStream.filter(track=[str(sys.argv[1])])
