import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

studyhrs = [1,2,3,4,5,6,7,8,9,10]
marks = [16,30,40,42,50,66,70,77,89,100]

plt.scatter(studyhrs, marks)
plt.show()
plt.plot(studyhrs, marks, 'r--')
plt.show()
plt.hist(marks)
plt.show()
plt.figure(figsize=(6,6))
plt.plot(studyhrs, marks, 'r-')
plt.plot(studyhrs, marks, 'bo')
plt.show()

plt.figure(figsize=(8,8))

plt.subplot(2,2,1)
plt.scatter(studyhrs, marks)
plt.subplot(2,2,2)
plt.plot(studyhrs, marks, 'r--')
plt.subplot(2,2,3)
plt.hist(marks)
plt.subplot(2,2,4)
plt.plot(studyhrs, marks, 'r-')
plt.plot(studyhrs, marks, 'bo')
plt.show()