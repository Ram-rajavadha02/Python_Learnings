import numpy as np

s1 = 'akshit is his name'
s2 = ' i am an Indian'

print(np.char.add(s1, s2))
print(np.char.upper(s1))    #makes all letters uppercase
print(np.char.lower(s1))
print(np.char.split(s1))    #split where it finds space

s3 = 'akshit is his \nname'
print(np.char.splitlines(s3))

print(np.char.replace(s1, 'name', 'surname'))

print('**********good bye************')
print(np.char.center('good bye', 40, '*'))