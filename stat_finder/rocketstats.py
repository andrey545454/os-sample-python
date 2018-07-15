from rls.rocket import RocketLeague

#работа с api от rocket league stats
def checker_stats(text):
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
    rocket = RocketLeague(api_key='5B5H59SRROQSENSZAHNHJM2XQ1VFKK1O')
    info = rocket.players.player(id=url, platform=1).json()
    rankedSeasons = info['rankedSeasons']
    currentSeason = rankedSeasons[max(rankedSeasons)]
    duelRank = Ranks[currentSeason['10']['tier']]+'({})'.format(currentSeason['10']['rankPoints'])
    doubleRank = Ranks[currentSeason['11']['tier']]+'({})'.format(currentSeason['11']['rankPoints'])
    soloStandartRank = Ranks[currentSeason['12']['tier']]+'({})'.format(currentSeason['12']['rankPoints'])
    StandartRank = Ranks[currentSeason['13']['tier']]+'({})'.format(currentSeason['13']['rankPoints'])
    return duelRank,doubleRank,soloStandartRank,StandartRank

#парсер по ссылке
def steam_url(text):
    index=text.find('id')+3
    if text[-1]=='/':
        return text[index:-1:]
    else:
        return text[index::]