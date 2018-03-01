import itchat
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


# login
itchat.auto_login(hotReload = True)
friends = itchat.get_friends(update = True)
#print(friends[0:3])

def analyseSex(friends):
    sexs = list(map(lambda x: x["Sex"], friends[1:]))
    print(sexs)
    counts = list(map(lambda x: x[1], Counter(sexs).items()))
    #a = Counter(sexs).items()
    #print(a)
    labels = ['Male', 'Female', 'Unknown']
    colors = ['red', 'yellowgreen', 'lightskyblue']
    plt.figure(figsize=(8,5), dpi = 80)
    plt.axes(aspect = 1)
    plt.pie(counts,
            labels = labels,
            colors = colors,
            labeldistance = 1.1,
            autopct = '%3.1f%%',
            shadow = False,
            startangle = 90,
            pctdistance = 0.6
            )
    plt.legend(loc = 'upper left')
    plt.title("QYQ nuo friends' gender distribution")
    plt.show()

analyseSex(friends)
