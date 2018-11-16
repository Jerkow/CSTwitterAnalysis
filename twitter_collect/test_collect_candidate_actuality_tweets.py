import twitter_collect as tc
import twitter_collect.collect_candidante_actuality_tweets as ccat

def test():
    assert ccat.get_candidates_accounts() == {'n': '@Emmanuelmacron'}
