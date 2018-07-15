import command_system
from datachecker import datacheck,usercheck
from random import randint

def spit(token,user_id,stroka='',peer_id=''):
    name=datacheck(token,user_id)
    if stroka!='':
        message=name+' плюнул в '+str(stroka).capitalize()+' '+'&#127773;'
    else:
        mas=usercheck(token,peer_id)['items']
        newmas=[]
        for user in mas:
            if user['member_id']!=user_id and user['member_id']>0:
                newmas.append(user)
        random_user=newmas[randint(0,len(newmas)-1)]['member_id']
        random_user=datacheck(token,random_user,'acc')
        message=name+' плюнул в '+str(random_user)+' '+'&#127773;'
    return message,''


spit_command=command_system.Command()
spit_command.keys=['!плюнь']
spit_command.description='Плюнуть в [Укажите в кого плюнуть]'
spit_command.process = spit