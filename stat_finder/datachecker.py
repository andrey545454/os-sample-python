# работа с vk.com
from vkapi import api


def name_check(token, user_id, name_case=''):  # Распознавание имени пользователя
    return api.users.get(access_token=token,user_ids=user_id, name_case=name_case)[0]['first_name']


def user_list_check(token,peer_id):  # Распознавание списка пользователей беседы
    return api.messages.getConversationMembers(access_token=token, peer_id=peer_id)
