import psycopg2
import redis
import json
import os

class Sender:
  def __init__(self):        
    self.__setup_redis_producer()
    self.__setup_database()

  def __setup_redis_producer(self):
    redis_host = os.getenv('REDIS_HOST', 'queue')
    redis_port = os.getenv('REDIS_PORT', 6379)
    redis_db = os.getenv('REDIS_DB', 0)
    self.queue = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)    

  def __setup_database(self):
    db_host = os.getenv('DB_HOST', 'mydbserver')
    db_user = os.getenv('DB_USER', 'postgres')
    db_name = os.getenv('DB_NAME', 'name_to_be_changed_by_env_example')
    dsn = f'dbname={db_name} user={db_user} host={db_host}'
    self.db_Connection = psycopg2.connect(dsn)

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