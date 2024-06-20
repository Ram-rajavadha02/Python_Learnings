import pandas as pd

df = pd.read_csv(r'/home/hp/pandas4.csv')
print(df.head())
print(df.isnull())      #to check whether dataframe has null values or not
print(df.isnull().sum())       #better way to check null value
print(df.shape)

df2 = df.dropna()       #default axis = 0
print(df2)
print(df2.shape)

df3 = df.dropna(axis = 1)       #axis = 1 for columns
print(df3)
print(df3.shape)

print(df.dropna(how = 'any'))   #if any row value is null then remove that row

print(df.dropna(inplace = True))
print(df.shape)