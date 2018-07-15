from rls.rocket import RocketLeague

#работа с api от rocket league stats
def checker_stats(text):
    url=steam_url(text)
    rocket = RocketLeague(api_key='5B5H59SRROQSENSZAHNHJM2XQ1VFKK1O')
    info = rocket.players.player(id=url, platform=1).json()
    rankedSeasons = info['rankedSeasons']
    currentSeason = rankedSeasons[max(rankedSeasons)]
    duelRank = currentSeason['10']['rankPoints']
    doubleRank = currentSeason['11']['rankPoints']
    soloStandartRank = currentSeason['12']['rankPoints']
    StandartRank = currentSeason['13']['rankPoints']
    return duelRank,doubleRank,soloStandartRank,StandartRank

#парсер по ссылке
def steam_url(text):
    index=text.find('id')+3
    if text[-1]=='/':
        return text[index:-1:]
    else:
        return text[index::]