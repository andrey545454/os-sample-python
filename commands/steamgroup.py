# команда для ссылки на стим группу покса
import command_system


def slink(token, user_id, stroka='', peer_id=''):
    message = 'Ссылочка на группу в Steam: '+r'https://www.twitch.tv/poqx'
    return message, ''


slink_command = command_system.Command()

slink_command.keys = ['!стим']
slink_command.description = 'Подскажу ссылку на группу в Steam'
slink_command.process = slink