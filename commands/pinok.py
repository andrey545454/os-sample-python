import command_system
from stat_finder.datachecker import datacheck, usercheck
from random import randint

def pinok(token,user_id,stroka='',peer_id=''):
    name=datacheck(token,user_id)
    #направленный пинок
    if stroka!='':
        message=name+' пнул '+str(stroka).capitalize()+' '+'&#127773;'
    #рандомный пинок
    else:
        user_list=usercheck(token,peer_id)['items']
        newmas=[]
        #фильтруем от ситуации когда пользователь пинает сам себя
        for user in user_list:
            if user['member_id']!=user_id and user['member_id']>0:
                newmas.append(user)
        random_user_id = newmas[randint(0,len(newmas)-1)]['member_id']
        random_user = datacheck(token,random_user_id, 'acc')
        message = name+' пнул @id'+str(random_user_id)+'({0})'.format(random_user)+'&#127773;'
    return message, ''

pinok_command=command_system.Command()
pinok_command.keys=['!пнуть']
pinok_command.description='Пнуть [укажите пользователя]'
pinok_command.process = pinok