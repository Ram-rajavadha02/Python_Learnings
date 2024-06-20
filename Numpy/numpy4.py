import numpy as np

a = np.arange(1,51)
a = a.reshape(10,5)
print(a)

print(a[0])     #prints only row 0 of a.

print(a[3,4].dtype)       #prints that particular element type.

print(a[0:10])      #prints all rows from 0 to 10.

print(a[0:5,2])     #prints all rows from 0 to 5 and elements of column 2.