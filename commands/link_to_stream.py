# команда для ссылки на стрим покса
import command_system
from stat_finder.datachecker import admins_list_check


def link(token, user_id, stroka='', peer_id=''):
    if user_id in admins_list_check(token, peer_id):
        message = 'Ссылка на твой стрим: https://www.twitch.tv/poqx'
    else:
        message = 'Ссылочка на стрим: https://www.twitch.tv/poqx'
    return message, ''


link_command = command_system.Command()

link_command.keys = ['!стрим']
link_command.description = 'Подскажу ссылку на стрим покса:)'
link_command.process = link