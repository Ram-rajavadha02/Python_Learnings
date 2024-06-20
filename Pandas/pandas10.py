import pandas as pd

df = pd.read_csv(r'/home/hp/Pandas/pandas7.csv', index_col=['Roll No.'])
print(df.head())

print(pd.pivot_table(df, index = 'Branch'))
print(pd.pivot_table(df, index = 'Branch', aggfunc='sum'))
print(pd.pivot_table(df, index = 'Branch', aggfunc='count'))
print(pd.pivot_table(df, index = 'Branch', columns = 'section'))