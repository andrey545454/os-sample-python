# файл с данными для работы бота с группой
# загружаем все локальные переменные с хостинга
from os import environ

token = environ.get('token')  # ключ доступа к сообществу
confirmation_token = environ.get('confirmation_token')  # ключ для настройки сервера с callback api
RLApi_token = environ.get('RLApi_token')  # ключ для доступа к rocket league stats api
