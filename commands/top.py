# команда для ссылки на топ чатеров
import command_system


def top(token, user_id, stroka='', peer_id=''):
    message = 'Ссылка на топ пользователей бота: http://chat-botik-andrey-bot.a3c1.starter-us-west-1.openshiftapps.com'
    return message, ''


top_command = command_system.Command()

top_command.keys = ['!топ']
top_command.description = 'Подскажу ссылку на топ пользователей бота'
top_command.process = top