# работа с vk.com
import vk

session = vk.Session()
api = vk.API(session, v=5.80)


def send_message(user_id, peer_id, token, message, attachment=""):  # функция для отправки сообщения пользователю
    if message != '':  # исключение отправки пустых сообщений
        if user_id != peer_id:
            api.messages.send(access_token=token, chat_id=peer_id-2000000000, message=message, attachment=attachment)
        else:
            api.messages.send(access_token=token, user_id=user_id, message=message, attachment=attachment)