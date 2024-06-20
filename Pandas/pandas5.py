import pandas as pd

df = pd.read_csv(r'/home/hp/Pandas/pandas4.csv')
print(df.isnull())
print(df.fillna(0))     #fills null value with zeros
print(df.fillna({'Physics':'none', 'Chemistry':0, 'Maths':30}))     #precise way of filling null values
print(df.fillna(method = 'ffill'))      #fills null value with previous value
print(df.fillna(method = 'ffill', axis = 0))    #consider previous value row wise
print(df.fillna(method = 'ffill', axis = 1))    #consider previous value column wise
print(df['Physics'].fillna(value=df['Physics'].mean()))

print(df.fillna(value = 'bfill'))       #fills null value with next value
print(df.fillna(method = 'bfill', inplace = True))
print(df)