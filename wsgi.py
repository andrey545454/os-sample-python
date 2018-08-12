# Мой файл для работы Flask приложения
from flask import Flask, request, json, render_template
import messageHandler
from settings.BD import get_info
from settings.settings import token, confirmation_token

application = Flask(__name__)


# декорирование функции для работы с пост запросами
@application.route("/bot", methods=['POST'])
def proccessing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        return 'ok'


# по приколу сделал
@application.route("/")
def table():
    mas, conn = get_info()
    return render_template('start_page.html', mas=mas)


# запуск приложения
if __name__ == "__main__":
    application.run()
