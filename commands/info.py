# команда для показа списка команд бота
import command_system


def info(token, user_id,stroka='', peer_id=''):
    message = ''
    for c in command_system.command_list:
        message += c.keys[0] + ' - ' + c.description + '\n'
    return message, ''


info_command = command_system.Command()

info_command.keys = ['!команды', 'команды', 'commands']
info_command.description = 'Покажу список команд'
info_command.process = info