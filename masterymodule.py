from riotwatcher import LolWatcher, ApiError

api_key = 'RGAPI-49ed4280-f63e-4267-aff2-8d89ad71f816'
watcher = LolWatcher(api_key)
my_region = 'eun1'


def masterycheck(name):
    me = watcher.summoner.by_name(my_region, name)
    score = watcher.champion_mastery.scores_by_summoner(my_region, me['id'])
    return score
