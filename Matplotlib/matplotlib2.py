import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

roll_no = [1,2,3,4,5,6,7,8,9,10]
marks = [10,20,30,40,50,60,70,80,90,100]

plt.plot(roll_no,marks,'r-')
plt.show()

plt.plot(roll_no,marks,linestyle = '--', color = '#728569') #color hascode
plt.show()

#for dotted line ':'
#for solid(default) line '-'
#for dashed line '--'
#for dashdot '-.'
#for None "or''

plt.plot(roll_no,marks,linestyle = '--',linewidth=10)
plt.show()


studyhrs = [1,2,3,4,5,6,7,8,9,10]
marks = [10,20,30,40,50,60,70,80,90,100]
plt.figure(figsize = (8,8))
plt.xticks(np.arange(0,10,1))
plt.yticks(np.arange(0,100,5))

plt.plot(studyhrs, marks, 'r-')
plt.plot(studyhrs, marks, 'bo')

plt.xlabel('Studyhrs')
plt.ylabel('Marks')
plt.show()