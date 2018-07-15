import vkapi
import os
import importlib
from command_system import command_list


def damerau_levenshtein_distance(s1, s2):
   d = {}
   lenstr1 = len(s1)
   lenstr2 = len(s2)
   for i in range(-1, lenstr1 + 1):
       d[(i, -1)] = i + 1
   for j in range(-1, lenstr2 + 1):
       d[(-1, j)] = j + 1
   for i in range(lenstr1):
       for j in range(lenstr2):
           if s1[i] == s2[j]:
               cost = 0
           else:
               cost = 1
           d[(i, j)] = min(
               d[(i - 1, j)] + 1,  # deletion
               d[(i, j - 1)] + 1,  # insertion
               d[(i - 1, j - 1)] + cost,  # substitution
           )
           if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
               d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition
   return d[lenstr1 - 1, lenstr2 - 1]


def load_modules():
   files = os.listdir("/home/andrey545454/mysite/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])


def get_answer(body,token,user_id,peer_id):
    message = ""
    attachment = ''
    distance = len(body)
    command = None
    key = ''
    for c in command_list:
        for k in c.keys:
            d = damerau_levenshtein_distance(body, k)
            if d < distance:
                distance = d
                command = c
                key = k
                if distance == 0:
                    message, attachment = c.process(token,user_id,message,peer_id)
                    return message, attachment
    if distance < len(body)*0.4:
        message, attachment = command.process(token,user_id,peer_id)
        message = 'Я понял ваш запрос как "%s"\n\n' % key + message
    return message, attachment

def get_answer2(body,stroka,token,user_id,peer_id):
    message = ""
    attachment = ''
    for c in command_list:
        if body in c.keys:
            message, attachment = c.process(token,user_id,stroka,peer_id)
    return message, attachment
def create_answer(data, token):
    #подгрузили модули
    load_modules()
    peer_id = data['peer_id']
    user_id = data['from_id']
    body=[str(s) for s in data['text'].lower().split(maxsplit=1)]
    if len(body)>1:
        message, attachment = get_answer2(body[0],body[1],token,user_id,peer_id)
    else:
        message, attachment = get_answer(data['text'].lower(),token,user_id,peer_id)
    vkapi.send_message(user_id,peer_id, token, message, attachment)