'''Coding = UTF-8
An unblock youku update script
default server:158.69.209.100
server:45.32.72.192
server:45.63.69.42
also can be used

'''

import requests
import re

f = open('rule.txt','w')
pac=requests.get('http://pac.uku.im/pac.pac').text
rexp='\,\"([a-z].+?[a-z])\"\:'
sites=re.findall(rexp,pac)
conf=''
for site in sites:
	rule=site+' = server:158.69.209.100\n'
	conf+=rule
print(conf)

f.write(conf)

f.close()
