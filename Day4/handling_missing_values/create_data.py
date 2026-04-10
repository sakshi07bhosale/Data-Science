import pandas as pd
import numpy as np 

data = {
    'Name':['Alice','Bob','Charlie','David','Eve'],
    'Age':[25,30,np.nan,35,40],
    'Salary':[50000,60000,70000,80000,90000],
    'City':['New York','Los Angeles','Chicago',np.nan,'Houston']
}

df = pd.DataFrame(data)
print(df)


print(df.isnull()) # to check missing values

print(df.isnull().sum()) # to check missing values count

df = df.dropna()
print(df) # to drop missing values

df = df.dropna(axis=1)
print(df) # to drop missing values

df.fillna(0, inplace=True)#to fill missing values with 0


df["Age"].fillna(21, inplace=True)  #to fill missing values with 21


