#Matching a String Against a Regular Expression With matches()

import re

st='an apple a day keeps a doctor away'
#in this string finding a word starts with 'a'
res=re.findall(r'a[\w]*',st)
print(res)
