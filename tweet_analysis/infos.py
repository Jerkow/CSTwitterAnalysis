"""
Informations pertinentes:
le tweet le plus retweeté
le plus liké
Moyenne de tous les RT
Evolution en fonction du temps (moyenne sur une heure de 7h à minuit)
"""
import numpy as np
import datetime as dt
import time
import twitter_collect.Data as Data
import pandas as pd
import matplotlib.pyplot as plt

def max_retweet(data):
    rt_max = np.max(data['RTs'])
    rt = data[data.RTs == rt_max].index[0]
    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))

def max_likes(data):
    likes_max = np.max(data['RTs'])
    like = data[data.Likes == likes_max].index[0]
    # Max Likes:
    print("The tweet with more likes is: \n{}".format(data['tweet_textual_content'][like]))
    print("Number of retweets: {}".format(likes_max))
    print("{} characters.\n".format(data['len'][like]))

"""
#Le but est de récupérer la moyenne des retweets des tweets publiés à une certaine heure
def recup_1h(data,date):
    jour, mois, annee, heure = date.day, date.month, date.year, date.hour
    listRetweets = []
    for i in range(len(data['tweet_textual_content'])):
        current_date = data['Date'][i]
        if [current_date.day, current_date.year, current_date.month, current_date.hour] == [jour, annee, mois, heure]:
            listRetweets.append(data['RTs'][i])
    return listRetweets

#On récupère un dictionnaire avec la moyenne sur chaque heure
def moyenne(data):
    dates = data['Date']
    dates_int = np.array([int(time.mktime(date.timetuple())) for date in dates ])
    debut, fin = min(dates_int), max(dates_int)
    heure_debut, heure_fin = debut-debut%3600, fin-fin%3600+3600
    dict = {}
    for i in range(heure_debut, heure_fin, 3600):
        liste = recup_1h(data, dt.datetime.fromtimestamp(i))
        dict[dt.datetime.fromtimestamp(i)] = sum(liste)/len(liste)
    return dict

print(data['Date'])
D = moyenne(data)
print(D)
"""
#On peut comparer la popularité de deux candidats
#EmmauelMacron
ax1 = plt.subplot(121)
ax1.set_title('Manu')
data = Data.collect_to_pandas_dataframe("@EmmanuelMacron")
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

#Donald Trump
ax2 = plt.subplot(122)
ax2.set_title('Donald')
data = Data.collect_to_pandas_dataframe("@realDonaldTrump")
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()
