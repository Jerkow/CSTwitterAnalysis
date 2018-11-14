import twitter_collect.twitter_collection_setup as connect


def collect(query):
    connexion = connect.twitter_setup()
    tweets = connexion.search(q=str(query), language="french", rpp=100)
    for tweet in tweets:
        print(tweet.text)


#collect('CentraleSupelec')

def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200, page =12)
    for status in statuses:
        print(status.text)
    return statuses

collect_by_user('@realDonaldTrump')

