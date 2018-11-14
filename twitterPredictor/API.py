import twitter_collect.twitter_collection_setup as connect

def collect():
    connexion = connect.twitter_setup()
    tweets = connexion.search("Emmanuel Macron", language="french", rpp=100)
    for tweet in tweets:
        print(tweet.text)

collect()
