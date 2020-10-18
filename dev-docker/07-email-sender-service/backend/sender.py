import psycopg2
import redis
import json

class Sender:
  def __init__(self):        
    self.__setup_redis_producer()
    self.__setup_database()

  def __setup_redis_producer(self):
    self.queue = redis.StrictRedis(host='queue', port=6379, db=0)    

  def __setup_database(self):
    DSN = 'dbname=email_sender user=postgres host=mydbserver'
    self.db_Connection = psycopg2.connect(DSN)

  def __register_message(self, subject, message):
    SQL = 'INSERT INTO emails (subject, message) VALUES (%s, %s)'
    cursor = self.db_Connection.cursor()
    cursor.execute(SQL, (subject, message));
    self.db_Connection.commit()
    cursor.close()
    print("Message has been registred!!")
  
  def __enqueue_message(self, subject, message):
    jsonMessage = json.dumps({'subject': subject, 'message': message})
    self.queue.rpush('sender', jsonMessage)
    print("Message has been enqueued!!!")

  def sendMessage(self, subject, message):
    self.__register_message(subject, message)
    self.__enqueue_message(subject, message)

    return 'Message has been sent!!!'