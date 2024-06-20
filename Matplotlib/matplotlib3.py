import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

subjects = ['Maths', 'English', 'Science', 'SS', 'Computer']
marks = [89, 96, 78, 95, 80]

plt.bar(subjects, marks)
plt.show()
plt.bar(subjects, marks, color = 'green')
plt.show()
colors = ['red','orange','yellow','green','blue']
plt.bar(subjects, marks, color = colors)
plt.show()
colors = ['red','orange','yellow','green','blue']
plt.bar(subjects, marks, color = colors, width = 0.5)
plt.show()
plt.bar(subjects, marks, color = colors, edgecolor = 'black')
plt.show()
plt.bar(subjects, marks, color = colors, edgecolor = 'black', linewidth = 4, linestyle = '-.')
plt.show()

plt.barh(subjects, marks)       #barh here h is for horizontal plot.
plt.show()

subjects = ['Maths', 'English', 'Science', 'SS', 'Computer']
marks1 = [89, 96, 78, 95, 80]
marks2 = [76, 86, 98, 85, 70]

plt.figure(figsize = (8,8))

subjects_len = np.arange(len(subjects))
width = 0.4
plt.bar(subjects_len, marks1, width = width, color = colors)
plt.bar(subjects_len + width, marks2, width = width, color = colors, alpha = 0.5)   #alpha is for transparency.

plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()