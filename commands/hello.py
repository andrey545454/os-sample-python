import command_system

def hello(token,user_id,stroka='',peer_id=''):
    message = 'Офф. группа бота(подписывайся):\n https://vk.com/club168452415'
    return message, ''

hello_command = command_system.Command()

hello_command.keys = ['!бот','!bot']
hello_command.description = 'Поприветствую тебя'
hello_command.process = hello