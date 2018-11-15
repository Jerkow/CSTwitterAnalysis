import tweet_analysis.infos as info
import datetime as dt

data = {'tweet_textual_content':['abcede','azoeiyrz'], 'len': [6,8], 'Likes':[12,0] ,'RTs':[492,89], 'created_at':["Thu Jul 28 00:08:39 +0000 2016","Thu Jul 28 01:07:39 +0000 2016"]}
str_date = "Thu Jul 28 00:08:00 +0000 2016"
date = dt.datetime.strptime(str_date[3:], ' %b %d %H:%M:%S +0000 %Y')

def test():
    assert info.recup_1h(data,date) == [492]
