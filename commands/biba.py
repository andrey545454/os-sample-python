# команда для прикола
import command_system
from random import randint


def biba(token, user_id, stroka='', peer_id=''):
    # подкрутка для меня
    if str(user_id) == '171859787':
        message = 'Твоя биба 100 см'
    # для всех остальных пользователей
    else:
        message = 'Твоя биба '+str(randint(1, 51))+'см'
    return message, ''


biba_command = command_system.Command()

biba_command.keys = ['!биба']
biba_command.description = 'Размер бибы'
biba_command.process = biba