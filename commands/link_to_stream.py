# команда для ссылки на стрим покса
import command_system
from vkapi import send_message
from settings.BD import get_info


def link(token, user_id, stroka='', peer_id=''):
    # рассылка если пишет покс
    if str(user_id) == '151635695':
        message = 'Пацаны залетаем на стрим к поксу: https://www.twitch.tv/poqx'
        list_of_subs = get_info('subs')
        for user in list_of_subs:
            send_message(user[0], user[0], token, message)
    # если команду пишет любой другой чел
    message = 'Ссылочка на стрим: https://www.twitch.tv/poqx'
    return message, ''


link_command = command_system.Command()

link_command.keys = ['!стрим']
link_command.description = 'Подскажу ссылку на стрим покса:)'
link_command.process = link