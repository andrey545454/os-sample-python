# Мой файл для работы Flask приложения
from flask import Flask,request,json
import messageHandler
from settings.settings import token,confirmation_token

application = Flask(__name__)

# декорирование функции для работы с пост запросами
@application.route("/", methods = ['POST'])
def proccessing():
    data=json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        return 'ok'

# по приколу сделал
@application.route("/hello")
def hello():
    return "Flask bot is live!"


# запуск приложения
if __name__ == "__main__":
    application.run()
