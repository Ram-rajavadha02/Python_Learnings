import pandas as pd

lst1 = [1, 2, 3, 4, 5, 6]
df = pd.DataFrame(lst1)
print(df)

lst2 = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]]
df = pd.DataFrame(lst2)
print(df)

a = [{'a':5, 'b':7, 'c':9, 'd':2},
     {'a':4, 'b':8, 'c':19, 'd':12}]
df = pd.DataFrame(a)
print(df)