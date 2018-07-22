# команда для распознавания степени хейта пользователя
import command_system
from random import randint
from stat_finder.datachecker import name_check


def hate(token, user_id, stroka='', peer_id=''):
    name = name_check(token,user_id)
    message = name+' ненавидит '+stroka+' на '+str(randint(1,100))+' %'
    return message, ''


hate_command=command_system.Command()
hate_command.keys=['!ненавижу']
hate_command.description='Узнай насколько ты ненавидишь [вставить нужное]'
hate_command.process = hate