from flask import Flask,request,json
from settings import *

application = Flask(__name__)

@application.route("/",methods=['POST'])
def proccessing():
    data=json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        return 'ok'

@application.route("/hello")
def hello():
    return "Hello Flask bot!"

if __name__ == "__main__":
    application.run()
