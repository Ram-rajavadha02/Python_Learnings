import numpy as np

a = np.arange(0,18).reshape((6,3))
b = np.arange(20,38).reshape((6,3))

print(a)
print(b)

print(a+b) #np.add(a,b)
print(a-b) #np.subtract(a,b)
print(a*b) #np.multiply(a,b)
print(a/b) #np.divide(a,b)

b = b.reshape((3,6))

print(a@b)  #print(a.dot(b)) same result

print(b.max())
print(b.min())

print(b.argmax())
print(np.sum(b))

print(np.sum(b, axis=1))

print(np.mean(b))
print(np.sqrt(b))
print(np.std(b))    #standard deviation all arrays.
print(np.log(b))