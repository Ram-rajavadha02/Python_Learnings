import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

roll_no = [1,2,3,4,5,6,7,8,9,10]
marks = [10,20,30,40,50,60,70,80,90,100]
plt.scatter(roll_no,marks,color='red',marker='*')
plt.show()

plt.figure(figsize = (12,8))
plt.scatter(roll_no,marks,color='blue',marker='*')
plt.show()

plt.figure(figsize = (8,8))
plt.plot(roll_no, marks, 'bo', markersize = 10)     #'bo' means blue colour o marker
plt.show()

temp_pune = [25,34,32,43,55,1,23,33,22,20]
humidity_pune = [23,24,42,33,42,23,42,22,11,22]

temp_bang = [26,33,36,33,25,11,43,33,12,40]
humidity_bang = [23,24,42,53,47,26,22,12,12,32]

plt.figure(figsize = (8,8))
plt.plot(temp_pune, humidity_pune, 'ro', markersize = 10)
plt.show()

#on same plot
plt.figure(figsize=(8,8))
plt.xticks(np.arange(0,60,5))
plt.yticks(np.arange(10,60,5))

plt.plot(temp_pune, humidity_pune, 'rv', markersize = 10)
plt.plot(temp_bang, humidity_bang, 'bo', markersize = 10)

plt.xlabel('Temoerature')
plt.ylabel('Humidity')
plt.show()