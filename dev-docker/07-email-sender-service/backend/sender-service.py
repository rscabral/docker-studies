import psycopg2
from flask import Flask, request, jsonify

DSN = 'dbname=email_sender user=postgres host=mydbserver'
SQL = 'INSERT INTO emails (subject, message) VALUES (%s, %s)'

def register_message(subject, message):
  db_Connection = psycopg2.connect(DSN)
  cursor = db_Connection.cursor()
  cursor.execute(SQL, (subject, message));
  db_Connection.commit()
  cursor.close()
  db_Connection.close()

  print("Message has been registred")

app = Flask(__name__);

@app.route('/', methods=['POST'])
def sendMessage():
  subject = request.form['subject']
  message = request.form['message']

  register_message(subject, message)

  return jsonify(message='Message has been sent!!!')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)