#data cleaning##how to handle missing data

import pandas as pd

data={
    "Name":['ram',None,'lolo','aditi','arsalan','raj','roman'],
    "Age":[23,43,None,45,78,54,33],
    "Salary":[5000,242342,56666,65432,89797,22222,224455],
    "Performance Score":[85,90,77,68,None,53,54]
}
df=pd.DataFrame(data)
print(df)
print("\n")

print(df.isnull())
print("\n")

#Now is we want to sum up the total missing elements:
print(df.isnull().sum())


##Now let's see how to HANDLE THE MISSING data for the betterment:
#We simply how to concepts: 1- removing 2-filling.

#for removing the rows or columns:
#We generally use this when the missing values are in same rows or columns and it will not matter if we remove them
#If any missing value is there , entire row or column will vanish depending on the axis (also inplace true means do changes in orginal data).

# df.dropna(axis=1, inplace=True)
# print(df)

#Now let's fill the missing data:

#df.fillna(Value,inplace =True)

#filling using a condition
df["Age"].fillna(df["Age"].mean(),inplace=True)
print(df)




