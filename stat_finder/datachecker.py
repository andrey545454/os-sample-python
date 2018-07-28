# работа с vk.com
from vkapi import api


def name_check(token, user_id, name_case=''):  # Распознавание имени пользователя
    return api.users.get(access_token=token,user_ids=user_id, name_case=name_case)[0]['first_name']


def user_list_check(token, peer_id):  # Распознавание списка пользователей беседы
    return api.messages.getConversationMembers(access_token=token, peer_id=peer_id)


def admins_list_check(token, peer_id):  # Список админов беседы (P.S на всякий случай)
    user_list = user_list_check(token, peer_id)
    admins_list = []
    for user in user_list:
        try:
            if int(user['member_id']) > 0:
                if user.get('is_admin') is not None:
                    admins_list.append(user['member_id'])
        except:
            print(user_list)
            break
    del user_list
    return admins_list
