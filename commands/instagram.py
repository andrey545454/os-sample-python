# команда для ссылки на инстаграм
import command_system


def instagram(token, user_id, stroka='',peer_id=''):
    message = 'Ссылочка на инсту: '+r'https://www.instagram.com/p.o.q.x/'
    return message, ''


instagram_command = command_system.Command()

instagram_command.keys = ['!инста']
instagram_command.description = 'Подскажу ссылку на инстаграм'
instagram_command.process = instagram