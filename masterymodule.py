from riotwatcher import LolWatcher, ApiError

api_key = 'RGAPI-776a6a6a-2d7f-4d67-96f6-4a3ee4bdcaeb'
watcher = LolWatcher(api_key)
my_region = 'eun1'


def masterycheck(name):
    me = watcher.summoner.by_name(my_region, name)
    score = watcher.champion_mastery.scores_by_summoner(my_region, me['id'])
    return score
