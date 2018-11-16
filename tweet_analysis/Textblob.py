from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB
from textblob.wordnet import Synset
import nltk
from twitter_collect import Data
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
