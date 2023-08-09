import matplotlib.pyplot as plt
import numpy as np
wordList = {'the':23135851162, 'of':13151942776, 'and':12997637966, 'to':12136980858, 'a':9081174698, 'in':8469404971, 'for':5933321709, 'is':4705743816, 'on':3750423199, 'that':3400031103}
title = "Most Common English Words\nGoogle Web Trillion Word Corpius"
colors = ('red','orange','green','blue','purple')


plt.bar(list(wordList.keys()),list(wordList.values()), color = colors)
plt.xlabel("English Word")
plt.ylabel("Number of Appearence")
plt.title(title)
plt.show()