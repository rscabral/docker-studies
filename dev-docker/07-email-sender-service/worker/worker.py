import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
  redis_consumer = redis.Redis(host='queue', port=6379, db=0)
  while True:
    message = json.loads(redis_consumer.blpop('sender')[1])
    # Simulator: Sending received email message from queue...
    print('Sending a message - Subject: {}; Message: {}'.format(message['subject'], message['message']))
    sleep(randint(5, 10))
    print('Message has been sent - Subject: {}; Message: {}!!!'.format(message['subject'], message['message']))