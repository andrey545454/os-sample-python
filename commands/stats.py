import command_system
from rocketstats import checker_stats


def stats(token,user_id,stroka='',peer_id=''):
    mas=checker_stats(stroka)
    message='1c- '+str(mas[0])+'  ,2c- '+str(mas[1])+'  ,3c- '+str(mas[2])+'  ,3cc- '+str(mas[3])
    return message,''


stats_command=command_system.Command()
stats_command.keys=['!стата']
stats_command.description='Узнать количество поинтов 1с, 2c, 3c, 3cc [нужно вставить ссылку на стим-аккаунт]'
stats_command.process = stats