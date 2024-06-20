import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

classes = ['Physics', 'Chemistry', 'Maths', 'science', 'SS']
marks = [89, 98, 76, 81, 90]

plt.pie(marks, labels = classes)
plt.show()

colors = ['red', 'blue', 'green', '#9803fc', '#03c2fc']

plt.pie(marks, labels = classes, colors=colors, autopct = '%0.1f%%')    #autopct shows percentage of each part.
plt.show()

explode_values = [0.1, 0, 0, 0, 0]

plt.pie(marks, labels=classes, colors=colors, autopct = '%0.2f%%', explode=explode_values, shadow=True)
plt.show()

plt.pie(marks, labels=classes, colors=colors, autopct = '%0.2f%%', explode=explode_values, radius = 1.6)
plt.show()

textprops = {'fontsize':14, 'color':'k'}
wedgeprops = {'linewidth':3, 'linestyle':'--', 'edgecolor':'white'}
plt.pie(marks, labels=classes, colors=colors, autopct = '%0.2f%%', textprops=textprops, wedgeprops=wedgeprops)
plt.legend()        #legend to describe color for which class.
plt.show()