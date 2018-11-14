import twitter_collect
from twitter_collect.twitter_collection_setup import twitter_setup

def test():
    assert twitter_setup() != None
