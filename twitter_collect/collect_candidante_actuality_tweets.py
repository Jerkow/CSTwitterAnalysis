import twitter_collect.twitter_collection_setup as connect
import tweepy
import sys
sys.path.insert(0, '../../')
import queries as q


def get_tweets_from_candidates_search_queries(queries, twitter_api):
    query_string = queries[0]
    for query in queries[1:]:
        query_string += 'OR'+query
    tweets = twitter_api.search(q=query_string, language="french",rpp=100)
    Tweet_list = [tweet.text for tweet in tweets]
    return Tweet_list

twitter_api = connect.twitter_setup()
queries = q.get_candidate_queries('n','../CandidateData/','keywords')
#queries = ['Emmanuel Macron']
print(get_tweets_from_candidates_search_queries(queries, twitter_api))
