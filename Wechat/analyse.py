'''
Thanks to http://blog.csdn.net/qinyuanpei/article/details/79360703 for the guidance
'''




import itchat
import jieba
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv

# login
itchat.auto_login(hotReload = True) # auto login
#itchat.login()
friends = itchat.get_friends(update = True)

def analyseSex(friends):
    sexs = list(map(lambda x: x["Sex"], friends[1:]))
    #print(sexs)
    counts = list(map(lambda x: x[1], sorted(Counter(sexs).items(), key = lambda x: x[0])))
    #a = Counter(sexs).items()
    #print(a)
    labels = ['Unknown', 'Male', 'Female']
    colors = ['lightskyblue', 'red', 'yellowgreen']
    plt.figure(figsize=(8,5), dpi = 80)
    plt.axes(aspect = 1)
    plt.pie(counts,
            labels = labels,
            colors = colors,
            labeldistance = 2.0,
            autopct = '%3.1f%%',
            shadow = False,
            startangle = 90,
            pctdistance = 0.6
            )
    plt.legend(loc = 'upper left')
    plt.title(u"%s nuo friends' gender distribution" % friends[0]['NickName'])
    plt.show()

def analyseLocation(friends):
    headers = ['NickName','Province','City']
    with open('location.csv','w',encoding='utf-8',newline='',) as csvFile:
        writer = csv.DictWriter(csvFile, headers)
        writer.writeheader()
        for friend in friends[1:]:
           row = {}
           row['NickName'] = friend['NickName']
           row['Province'] = friend['Province']
           row['City'] = friend['City']
           writer.writerow(row)



if __name__ == '__main__':
    analyseSex(friends)
    analyseLocation(friends)
