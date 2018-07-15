import command_system
from stat_finder.datachecker import datacheck, usercheck
from random import randint

def pinok(token,user_id,stroka='',peer_id=''):
    name=datacheck(token,user_id)
    if stroka!='':
        message=name+' пнул '+str(stroka).capitalize()+' '+'&#127773;'
    else:
        mas=usercheck(token,peer_id)['items']
        newmas=[]
        for user in mas:
            if user['member_id']!=user_id and user['member_id']>0:
                newmas.append(user)
        random_user=newmas[randint(0,len(newmas)-1)]['member_id']
        random_user=datacheck(token,random_user,'acc')
        message=name+' пнул '+str(random_user)+' '+'&#127773;'
    return message,''

pinok_command=command_system.Command()
pinok_command.keys=['!пнуть']
pinok_command.description='Пнуть пользователя'
pinok_command.process = pinok