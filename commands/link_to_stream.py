# команда для ссылки на стрим покса
import command_system
from vkapi import send_message
from stat_finder.datachecker import admins_list_check,list_of_subs


def link(token, user_id, stroka='', peer_id=''):
    # проверка на админа чтобы запустить расссылку
    if user_id in admins_list_check(token, peer_id):
        list_of_users = list_of_subs(token, peer_id)['users']
        message = r'Стример на Поксе подрубил стрим: https://www.twitch.tv/poqx (тест)'
        # отправление сообщения каждому пользователю
        for user in list_of_users:
            send_message(user, user, token, message)
    else:
        message = 'Ссылочка на стрим: https://www.twitch.tv/poqx'
    return message, ''


link_command = command_system.Command()

link_command.keys = ['!стрим']
link_command.description = 'Подскажу ссылку на стрим покса:)'
link_command.process = link