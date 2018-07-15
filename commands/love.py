import command_system
from random import randint
from stat_finder.datachecker import datacheck

def love(token,user_id,stroka='',peer_id=''):
    name=datacheck(token,user_id)
    message=name+' любит '+stroka+' на '+str(randint(1,100))+' %'
    return message,''

love_command=command_system.Command()
love_command.keys=['!люблю']
love_command.description='Узнай насколько ты любишь [вставить нужное]'
love_command.process = love