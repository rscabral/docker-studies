import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
  redis_host = os.getenv('REDIS_HOST', 'queue')
  redis_port = os.getenv('REDIS_PORT', 6379)
  redis_db = os.getenv('REDIS_DB', 0)
  redis_consumer = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

  print('Waiting messages from queue...')
  
  while True:
    message = json.loads(redis_consumer.blpop('sender')[1])
    # Simulator: Sending received email message from queue...
    print('Sending a message - Subject: {}; Message: {}'.format(message['subject'], message['message']))
    sleep(randint(5, 10))
    print('Message has been sent - Subject: {}; Message: {}!!!'.format(message['subject'], message['message']))