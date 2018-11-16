import twitter_collect.twitter_collection_setup as connect
import numpy as np
import pandas as pd


def collect_to_pandas_dataframe(candidat):
    connexion = connect.twitter_setup()
    #tweets = connexion.search(candidat,language="fr",rpp = 1000, pages=100)
    tweets = connexion.search(candidat, language="en",rpp = 1000, pages=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']    = np.array([len(tweet.text) for tweet in tweets])
    data['ID']     = np.array([tweet.id for tweet in tweets])
    data['Date']   = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data
