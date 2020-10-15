from flask import Flask, request, jsonify

app = Flask(__name__);

@app.route('/', methods=['POST'])
def sendMessage():
  subject = request.form['subject']
  message = request.form['message']
  return jsonify(subject=subject, message=message)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)