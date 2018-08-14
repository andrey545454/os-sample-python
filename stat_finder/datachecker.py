# работа с vk.com
from vkapi import api


def name_check(token, user_id, name_case=''):
    """Распознавание имени пользователя"""
    return api.users.get(access_token=token, user_ids=user_id, name_case=name_case)[0]['first_name']


def name_and_surname(token, user_id, name_case=''):
    """Распознавание имени и фамилии пользователя"""
    return api.users.get(access_token=token, user_ids=user_id, name_case=name_case)[0]['first_name'], \
           api.users.get(access_token=token, user_ids=user_id, name_case=name_case)[0]['last_name']


def user_list_check(token, peer_id):
    """Распознавание списка пользователей беседы"""
    return api.messages.getConversationMembers(access_token=token, peer_id=peer_id)


def admins_list_check(token, peer_id):
    """Список админов беседы (P.S на всякий случай)"""
    user_list = user_list_check(token, peer_id)['items']  # айдишки находятся в items
    admins_list = []
    for user in user_list:
        if int(user['member_id']) > 0:
            if user.get('is_admin') is not None:
                admins_list.append(user['member_id'])
    del user_list  # подчистим память
    return admins_list


def list_of_subs(token, peer_id):
    """Список участников группы"""
    return api.groups.getMembers(access_token=token, group_id='168452415')


def user_is_member(token, user_id):
    """Проверка на участника группы"""
    api.groups.isMember(access_token=token, group_id='168452415', user_id=user_id)


def blacklist(user_id, black_list_table):
    for x in black_list_table:
        if x[0] == user_id:
            return True
    else:
        return False