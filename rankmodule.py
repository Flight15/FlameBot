from riotwatcher import LolWatcher, ApiError

api_key = 'RGAPI-49ed4280-f63e-4267-aff2-8d89ad71f816'
watcher = LolWatcher(api_key)
my_region = 'eun1'


# print("summoner name")


def rankcheck(name):
    me = watcher.summoner.by_name(my_region, name)
    ranked = watcher.league.by_summoner(my_region, me['id'])
    if ranked[0]['queueType'] == 'RANKED_SOLO_5x5':
        rankedcomb = format(ranked[0]['tier']) + ' ' + format(ranked[0]['rank'])
    elif ranked[1]['queueType'] == 'RANKED_SOLO_5x5':
        rankedcomb = format(ranked[1]['tier']) + ' ' + format(ranked[1]['rank'])
    else:
        rankedcomb = format(ranked[2]['tier']) + ' ' + format(ranked[2]['rank'])
    return rankedcomb
   # return ranked[0]['tier']['rank']


'''me = watcher.summoner.by_name(my_region, input())
ranked = watcher.league.by_summoner(my_region, me['id'])
if (ranked[1]['tier']) == "IRON" or (ranked[1]['tier']) == "BRONZE" or (ranked[1]['tier']) == "SILVER":
    print("you are low ELO trash")
    print("your rank is " + ranked[1]['tier'])
else:
    print("you are not low elo trash")
    print("your rank is " + ranked[1]['tier'])
if ranked[1]['veteran']:
    print("you're hardstuck")
else:
    print("you're not hardstuck")'''
