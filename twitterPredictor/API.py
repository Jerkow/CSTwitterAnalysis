import twitter_collect.twitter_collection_setup as connect
import tweepy

def collect(query):
    connexion = connect.twitter_setup()
    tweets = connexion.search(q=str(query), language="french", rpp=100)
    for tweet in tweets:
        print(tweet.text)


#collect('CentraleSupelec')

def collect_by_user(user_id):
    connexion = connect.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200, page =11)
    for status in statuses:
        print(status.text)
    return statuses

#collect_by_user('25073877')

from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True

def collect_by_streaming():
    connexion = connect.twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener, language="french")
    stream.filter(track=['Emmanuel Macron'])

collect_by_streaming()
