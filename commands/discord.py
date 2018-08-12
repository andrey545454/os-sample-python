# команда для ссылки на дискорд канал
import command_system


def discord(token, user_id, stroka='', peer_id=''):
    message = 'Ссылочка на дискорд канал: https://discord.gg/Hv47uYA'
    return message, ''


discord_command = command_system.Command()

discord_command.keys = ['!дискорд']
discord_command.description = 'Подскажу ссылку на дискорд канал'
discord_command.process = discord
