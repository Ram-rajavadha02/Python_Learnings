import numpy as np

print(np.random.random(1))
print(np.random.random(2))
print(np.random.random((2,2)))

a = np.arange(1,10)
print(a)

print(np.random.choice(a))  #or else print(np.random.randint(1,10))

print(np.random.randint(1,20, (2,2)))

print(np.random.rand(2,2))  #gives float value same as random
print(np.random.randn(2,2)) #also help get negative value