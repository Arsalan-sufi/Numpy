#step-1 sample dataframe

import pandas as pd

data={
    "Name":['ram','ghanshyam','lolo','aditi','arsalan','raj','roman'],
    "Age":[23,43,21,45,78,54,33],
    "Salary":[5000,242342,56666,65432,89797,22222,224455],
    "Performance Score":[85,90,77,68,87,53,54]
}
df=pd.DataFrame(data)

print("Sample Dataframe")
print(df)
#we can update entire column or entires satisfying a certain condition

df.loc[df["Salary"] < 75000, "Salary"] *= 1.25
print(df)

#for entire column:
df["Performance Score"]=df["Performance Score"]*1.05
print(df)

##Removing columns
df.drop(columns=["Performance Score","Age"],inplace=True)
print(df)