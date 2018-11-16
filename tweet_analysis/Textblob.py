from textblob import TextBlob

"""
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
nltk.download('wordnet')
"""

#On crée la liste des stop words pour pouvoir les enlever des tweets par la suite
stop_words = TextBlob("""alors
au
aucuns
aussi
autre
avant
avec
avoir
bon
car
ce
cela
ces
ceux
chaque
ci
comme
comment
dans
des
du
dedans
dehors
depuis
devrait
doit
donc
dos
début
elle
elles
en
encore
essai
est
et
eu
fait
faites
fois
font
hors
ici
il
ils
je	juste
la
le
les
leur
là
ma
maintenant
mais
mes
mine
moins
mon
mot
même
ni
nommés
notre
nous
ou
où
par
parce
pas
peut
peu
plupart
pour
pourquoi
quand
que
quel
quelle
quelles
quels
qui
sa
sans
ses
seulement
si
sien
son
sont
sous
soyez	sujet
sur
ta
tandis
tellement
tels
tes
ton
tous
tout
trop
très
tu
voient
vont
votre
vous
vu
ça
étaient
état
étions
été
être
de ne c'est ont http cet cette cesa à l y Je un plus le... 1 2 3 4 5 6 7 8 9 p qu'on pa une d d'qu' n'a
""").words

def vocabulaire(data):
    """
    :param data: all the tweets that have been collected
    :return: the set of the vocabulary used in the tweets
    """
    tweets = data['tweet_textual_content'] #On récupère les tweets
    words_tweets = [TextBlob(tweet).words.lemmatize() for tweet in tweets] #On prend les mots de chaque tweet
    word_set = set()
    for tweet in words_tweets:
        word_set.update(tweet)
    #On en fait un ensemble pour enlever les doublons
    for stop_word in stop_words:
        word_set.discard(stop_word)
    #On supprime les stop words
    return word_set

"""
Petit test : 

data = Data.collect_to_pandas_dataframe('@EmmanuelMacron')
print([vocabulaire(data)])
"""

def polarity(tweet):
    """
    :param tweet: a string representing a tweet
    :return: 0 if the tweet is neutral
            -1 if the tweet is negative
            +1 if the tweet is positive
    """
    if TextBlob(tweet).detect_language() != 'en':
        polar = TextBlob(tweet).translate(to='en').sentiment.polarity
    else:
        polar = TextBlob(tweet).sentiment.polarity
    if polar < -1/9:
        return -1
    elif polar > 1/9:
        return 1
    else:
        return 0

def opinion(data):
    """
    :param data: The data collected on twitter
    :return: three integers:
            pos_tweets : the number of positive tweets
            neu_tweets : the number of neutral tweets
            neg_tweets : the number of negative tweets
    """
    pos_tweets, neu_tweets, neg_tweets = [], [], []
    Tweets = data['tweet_textual_content']
    for tweet in Tweets:
        if polarity(tweet) < 0:
            neg_tweets.append(tweet)
        elif polarity(tweet) > 0:
            pos_tweets.append(tweet)
        else:
            neu_tweets.append(tweet)
    return pos_tweets, neu_tweets, neg_tweets

"""
data = Data.collect_to_pandas_dataframe('@EmmanuelMacron')

pos_tweets, neu_tweets, neg_tweets = opinion(data)
print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))
"""
