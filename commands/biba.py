import command_system
from random import randint

def biba(token,user_id,stroka='',peer_id=''):
    message='Твоя биба '+str(randint(2,50))+'см'
    return message,''

biba_command=command_system.Command()
biba_command.keys=['!биба']
biba_command.description='Размер бибы'
biba_command.process = biba