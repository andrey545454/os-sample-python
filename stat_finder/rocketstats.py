# файл для работы с rocketleaguestats.com
from rls.rocket import RocketLeague
from settings.settings import RLApi_token


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


def steam_url(text):  # парсер по ссылке steam профиля для распознавания id
    index=text.find('id')+3
    # если в конце ссылки присутствует / то убираем её
    if text[-1]=='/':
        return text[index:-1:]
    else:
        return text[index::]