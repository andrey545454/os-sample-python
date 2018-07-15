from vkapi import api

def datacheck(token,user_id,name_case=''):
    return api.users.get(access_token=token,user_ids=user_id, name_case=name_case)[0]['first_name']

def usercheck(token,peer_id):
    return api.messages.getConversationMembers(access_token=token,peer_id=peer_id)