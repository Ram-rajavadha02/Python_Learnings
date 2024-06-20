import pandas as pd

df = pd.read_csv(r'/home/hp/Pandas/pandas7.csv', index_col=['Roll No.'])
print(df.head())
branch_group = df.groupby(by = 'Branch')
print(branch_group)
print(branch_group.groups)

branch_group = df.groupby(by = ['Branch', 'Maths'])
print(branch_group.groups)

for group, data_frame in branch_group:
    print(group)
    print(data_frame)

df1 = pd.DataFrame({'Roll No.':[1, 2, 3, 4, 5], 'Physics':[32,34,54,21,43]})
print(df1)
df2 = pd.DataFrame({'Roll No.':[1, 2, 3, 4, 5], 'Chemistry':[22,35,85,65,89]})
print(df2)
print(pd.merge(df1, df2, on = 'Roll No.'))

df3 = pd.DataFrame({'Roll No.':[6, 7, 2, 5, 9], 'Chemistry':[22,35,85,65,89]})
print(df3)
print(pd.merge(df1, df3, how = 'left'))
print(pd.merge(df1, df3, how = 'right'))
print(pd.merge(df1, df3, how = 'outer'))