import pandas as pd

df = pd.read_csv(r'/home/hp/Pandas/pandas7.csv', index_col=['Roll No.'])
print(df.head())
print(df.loc[1])
print(df.loc[5])
print(df.loc[5:10, 'Chemistry'])
print(df.loc[df['Physics']>30, ['Maths']])

print(df.iloc[0])   #iloc is for index and loc check rollno
print(df.iloc[[0,1,2]])
print(df.iloc[:,1])
print(df.iloc[0:5,1:4])