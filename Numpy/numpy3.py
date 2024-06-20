import numpy as np

a = np.arange(1,20)
print(a)

a = np.arange(2,20,2)
print(a)

a = a.reshape((3,3))
print(a)

b = np.arange(1,100,2)
print(b)

b = b.reshape((10,5))
print(b)

b = b.flatten() #returns copy of that array
print(b)

b = b.ravel()   #returns copy of that original array
print(b)