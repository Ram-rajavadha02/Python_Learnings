import pandas as pd

df = pd.read_csv(r'/home/hp/Pandas/pandas4.csv')
print(df.head())
print(df.replace(to_replace = 54, value = 10))
print(df.replace(54,100))
print(df.replace(to_replace = [45,54,65], value = 1))
print(df.replace(to_replace = [45,54,65], value = ['a', 'b', 'c']))
print(df.replace('[A-Za-z]', 0, regex = True))
print(df.replace(to_replace = 54, method = 'ffill'))