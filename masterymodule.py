from riotwatcher import LolWatcher, ApiError

api_key = 'RGAPI-c5692ce3-e7c3-46e4-aedb-4c204853075d'
watcher = LolWatcher(api_key)
my_region = 'eun1'


def masterycheck(name):
    me = watcher.summoner.by_name(my_region, name)
    score = watcher.champion_mastery.scores_by_summoner(my_region, me['id'])
    return score
