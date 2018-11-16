from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB
from textblob.wordnet import Synset
import nltk
from twitter_collect import Data

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
nltk.download('wordnet')

def vocabulaire(data):
    tweets = data['tweet_textual_content']
    words = [TextBlob(tweet).words for tweet in tweets]
    return words

data = Data.collect_to_pandas_dataframe('@EmmanuelMacron')

print([vocabulaire(data)])
