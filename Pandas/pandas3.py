import pandas as pd

df = pd.read_csv(r'/home/hp/pandas.csv')
print(df.columns)
print(df.shape)
print(df.size)

print(df.head())        #by default first 5 rows, head for first
print(df.head(2))       #print first 2 rows

print(df.tail())        #by default last 5 rows, tail for last
print(df.describe())        #gives data about count, mean, std, min, 25%, 50%, 75%, max.
print(df.info())        #info abt non-null values, entries, total columns, dtypes, memory.