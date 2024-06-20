import pandas as pd

df1 = pd.DataFrame({'Roll No.':[1, 2, 3, 4, 5], 'Maths':[45, 65, 87, 75, 95], 'Physics':[32,34,54,21,43]})
print(df1)
df2 = pd.DataFrame({'Roll No.':[6, 7, 8, 9, 10], 'Maths':[55, 75, 27, 65, 72], 'Physics':[82,14,44,29,93]})
print(df2)

print(df1.append(df2))      #df2 is next to df1
print(df2.append(df1))      #df1 is next to df2
print(df1.append(df2, ignore_index = True))
print(df1.append(df2, ignore_index = True, sort = True))