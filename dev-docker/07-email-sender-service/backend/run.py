from routes import blueprint
from flask import Flask

app = Flask(__name__)
app.register_blueprint(blueprint)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)