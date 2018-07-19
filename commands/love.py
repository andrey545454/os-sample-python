# команда для распознавания степени любви пользователя
import command_system
from random import randint
from stat_finder.datachecker import name_check


def love(token, user_id, stroka='', peer_id=''):
    name = name_check(token,user_id)
    message = name+' любит '+stroka+' на '+str(randint(1,100))+' %'
    return message, ''


love_command=command_system.Command()
love_command.keys=['!люблю']
love_command.description='Узнай насколько ты любишь [вставить нужное]'
love_command.process = love