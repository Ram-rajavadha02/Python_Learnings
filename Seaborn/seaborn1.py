import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

roll_no = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
marks = [23,43,23,44,56,66,34,54,76,45,21,44,55,67,88]
sample_df = pd.DataFrame({"Roll_no": roll_no, "Marks": marks})
print(sample_df.head())

sns.lineplot(x= 'Roll_no', y= 'Marks', data=sample_df)
plt.title('Student Marks')