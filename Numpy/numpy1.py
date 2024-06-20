import numpy as np

lst = [1, 2, 3, 4, 5]
print(lst)

print('1D Array')
a = np.array([1, 2, 3, 4, 5])
print(a)

print('2D Array')
b = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10]])
print(b)

print('3D Array')
c = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]])
print(c)

type(a)
print(a.size)
print(a.shape)
print(a.dtype)

print(c.transpose())