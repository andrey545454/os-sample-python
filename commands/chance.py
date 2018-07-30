# команда для распознавания шанса
import command_system
from random import randint


def chance(token,user_id,stroka='',peer_id=''):
    message = 'Шанс равен '+str(randint(1, 100))+'%'
    return message, ''

chance_command = command_system.Command()

chance_command.keys = ['!шанс']
chance_command.description = 'Узнай шанс чего-либо'
chance_command.process = chance
