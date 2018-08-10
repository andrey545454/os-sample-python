# команда для ссылки на стрим покса
import command_system
from vkapi import send_message
from stat_finder.datachecker import admins_list_check,list_of_subs


def link(token, user_id, stroka='', peer_id=''):
    message = 'Ссылочка на стрим: https://www.twitch.tv/poqx'
    return message, ''


link_command = command_system.Command()

link_command.keys = ['!стрим']
link_command.description = 'Подскажу ссылку на стрим покса:)'
link_command.process = link