from flask import Blueprint, request, jsonify
from sender import Sender

blueprint = Blueprint('sender', __name__)
  
@blueprint.route('/', methods=['POST'])
def sendMessage():
  sender = Sender()
  subject = request.form['subject']
  message = request.form['message']
  returnedMessage = sender.sendMessage(subject=subject, message=message)
  return jsonify(returnedMessage)