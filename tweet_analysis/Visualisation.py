"""
Grouped barplots
================

_thumb: .45, .5
"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import tweet_analysis.Textblob as TB
from twitter_collect import Data

sns.set(style="whitegrid")

f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(7, 5), sharex=True)
#On affiche les barres 'positif', 'négatif", 'neutre' pour Macron, Trump et Le Pen
x = np.array(['Positive', 'Neutral', 'Negative'])
data1 = Data.collect_to_pandas_dataframe('@EmmanuelMacron')
Tuple1 = TB.opinion(data1)
y1 = [len(liste) for liste in Tuple1]
sns.barplot(x=x, y=y1, palette="rocket", ax=ax1)
ax1.axhline(0, color="k", clip_on=False)
ax1.set_ylabel("@EmmanuelMacron")

data2 = Data.collect_to_pandas_dataframe('@realDonaldTrump')
Tuple2 = TB.opinion(data2)
y2 = [len(liste) for liste in Tuple2]
sns.barplot(x=x, y=y2, palette="vlag", ax=ax2)
ax2.axhline(0, color="k", clip_on=False)
ax2.set_ylabel("@realDonaldTrump")

data3 = Data.collect_to_pandas_dataframe('@lepen')
Tuple3 = TB.opinion(data3)
y3 = [len(liste) for liste in Tuple3]
sns.barplot(x=x, y=y3, palette="vlag", ax=ax3)
ax3.axhline(0, color="k", clip_on=False)
ax3.set_ylabel("@lepen")

# Draw a nested barplot to show survival for class and sex
sns.despine(bottom=True)
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)
plt.show()

