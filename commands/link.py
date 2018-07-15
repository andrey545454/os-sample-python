import command_system

def link(token,user_id,stroka='',peer_id=''):
    message = 'Ссылочка на стрим: '+r'https://www.twitch.tv/poqx'
    return message, ''

link_command = command_system.Command()

link_command.keys = ['!стрим']
link_command.description = 'Подскажу ссылку на стрим покса:)'
link_command.process = link