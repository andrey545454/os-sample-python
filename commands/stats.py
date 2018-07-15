import command_system
from rocketstats import checker_stats


def stats(token,user_id,stroka='',peer_id=''):
    mas=checker_stats(stroka)
    message=str(mas)
    return message,''


stats_command=command_system.Command()
stats_command.keys=['!стата']
stats_command.description='Узнать количество поинтов 1с, 2c, 3c, 3cc [нужно вставить ссылку на стим-аккаунт][НЕ РАБОТАЕТ]'
stats_command.process = stats