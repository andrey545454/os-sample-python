# команда для подписки на рассылку стримов
import command_system
from settings.BD import get_info, set_info


def subscribe(token, user_id, stroka='', peer_id=''):
    # проверяем пишет ли пользователь в лс группы
    if str(user_id) != str(peer_id):
        message = 'Напишите эту команду в лс: https://vk.com/write-168452415'
    # если да то проверяем подписан ли он уже
    else:
        list_of_subs = get_info('subs')
        for sub in list_of_subs:
            if sub[0] == str(user_id):
                message = 'Вы уже подписаны на оповещения'
                break
        # не подписан - значит подписываем
        else:
            set_info(bdname='subs', user_id=str(user_id))
            message = 'Вы подписались на оповещения о стримах :)'
    return message, ''


subscribe_command = command_system.Command()

subscribe_command.keys = ['!подписаться']
subscribe_command.description = 'Команда для подписки на рассылку стримов покса \n ' \
                                '(пишите команду в лс: https://vk.com/write-168452415)'
subscribe_command.process = subscribe