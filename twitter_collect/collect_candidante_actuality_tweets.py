import twitter_collect.twitter_collection_setup as connect
import queries as q

def get_tweets_from_candidates_search_queries(queries, twitter_api):
    queries_str = queries[0]
    for query in queries[1:]:
        queries_str = queries_str + ' OR ' + query
    tweets = twitter_api.search(q=str(queries_str), language="french", count=100)
    tweet_list=[tweet.text for tweet in tweets]
    return(tweet_list)

twitter_api = connect.twitter_setup()
print(get_tweets_from_candidates_search_queries(['@EmmanuelMacron'], twitter_api))

"""
On doit d'abord faire le lien entre le numéro du candidat et son compte twitter
On suppose quon a cette information dans un fichier texte sous la forme :
num_candidat : @comptecandidat
"""

def get_candidates_accounts():
    try:
        fichier = open('../CandidateData/candidates_twitter_account.txt','rt')
        dict = {}
        for ligne in fichier:
            code = ''
            for i in range(len(ligne)):
                if ligne[i] != ' ':
                    code += ligne[i]
                else: break
            candidat = ligne[i+3:]
            dict[code] = candidat
        return dict
    except IOError:
        "Erreur de fichier"

print(get_candidates_accounts())

