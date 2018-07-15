import command_system

def group(token,user_id,stroka='',peer_id=''):
    message = 'Ссылочка на группу ВК: '+r'https://vk.com/poqxclub'
    return message, ''

group_command = command_system.Command()

group_command.keys = ['!группа']
group_command.description = 'Подскажу ссылку на группу ВК'
group_command.process = group