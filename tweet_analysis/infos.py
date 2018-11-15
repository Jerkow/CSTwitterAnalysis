"""
Informations pertinentes:
le tweet le plus retweeté
le plus liké
Moyenne de tous les RT
Evolution en fonction du temps (moyenne sur une heure de 7h à minuit)
"""
import numpy as np
import datetime as dt

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

def recup_1h(data,date):
    jour, mois, annee, heure = date.day, date.month, date.year, date.hour
    listRetweets = []
    for i in range(len(data['tweet_textual_content'])):
        str_date = data['created_at'][i]
        current_date = dt.datetime.strptime(str_date[3:], ' %b %d %H:%M:%S +0000 %Y')
        if [current_date.day, current_date.year, current_date.month, current_date.hour] == [jour, annee, mois, heure]:
            listRetweets.append(data['RTs'][i])
    return listRetweets
data = {'tweet_textual_content':['abcede','azoeiyrz'], 'RTs':[492,89], 'created_at':["Thu Jul 28 00:08:39 +0000 2016","Thu Jul 28 01:07:39 +0000 2016"]}
str_date = "Thu Jul 28 00:08:00 +0000 2016"
date = dt.datetime.strptime(str_date[3:], ' %b %d %H:%M:%S +0000 %Y')
print(recup_1h(data, date))
