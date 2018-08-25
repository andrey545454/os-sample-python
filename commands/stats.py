# команда для рангов с rocket league stats
import command_system
from stat_finder.rocketstats import checker_stats


def stats(token, user_id, stroka='', peer_id=''):
    try:
        mas = checker_stats(stroka)
        message = '1c- '+str(mas[0])+'\n,2c- '+str(mas[1])+'\n,3cc- '+str(mas[2])+'\n,3c- '+str(mas[3])
    except:
        message = 'Что-то пошло не так!'
    return message, ''


stats_command = command_system.Command()
stats_command.keys = ['!стата']
stats_command.description = 'Узнать количество поинтов 1с, 2c, 3c, 3cc [нужно вставить ссылку на стим-аккаунт]'
stats_command.process = stats