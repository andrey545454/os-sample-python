# файл для работы с rocketleaguestats.com
from re import findall
from rls.rocket import RocketLeague
from settings.settings import RLApi_token


def steam_url(text):  # парсер по ссылке steam профиля для распознавания id
    if findall('/id/', text):  # если ссылка содержить '/id/'
        id = text.index('/id/')
        if text[-1] == '/':  # если ссылка содержит '/' в конце
            return text[id + 4:-1:]
        else:
            return text[id + 4:]
    else:  # иначе в ссылке есть '/profiles/'
        id = text.index('/profiles/')
        if text[-1] == '/':  # если ссылка содержит '/' в конце
            return text[id + 10:-1:]
        else:
            return text[id + 10:]

def checker_stats(text):  # распознавание рангов пользователя
    # массив возможных рангов
    Ranks=['Unranked',
           'Bronze I',
           'Bronze II',
           'Bronze III',
           'Silver I',
           'Silver II',
           'Silver III',
           'Gold I',
           'Gold II',
           'Gold III',
           'Platinum I',
           'Platinum II',
           'Platinum III',
           'Diamond I',
           'Diamond II',
           'Diamond III',
           'Champion I',
           'Champion II',
           'Champion III',
           'Grand Champion'
           ]
    url=steam_url(text)
    rocket = RocketLeague(api_key=RLApi_token)
    info = rocket.players.player(id=url, platform=1).json()
    rankedSeasons = info['rankedSeasons']
    currentSeason = rankedSeasons[max(rankedSeasons)]
    duelRank = Ranks[currentSeason['10']['tier']]+'({})'.format(currentSeason['10']['rankPoints'])
    doubleRank = Ranks[currentSeason['11']['tier']]+'({})'.format(currentSeason['11']['rankPoints'])
    soloStandartRank = Ranks[currentSeason['12']['tier']]+'({})'.format(currentSeason['12']['rankPoints'])
    StandartRank = Ranks[currentSeason['13']['tier']]+'({})'.format(currentSeason['13']['rankPoints'])
    return duelRank,doubleRank,soloStandartRank,StandartRank
