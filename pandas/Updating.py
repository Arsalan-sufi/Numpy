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
print("\n")

#here we will update the salary of ram
#Syntax: df.loc[row_index, "Column Name"]= upadated_Value
df.loc[0,"Salary"]=70000
print(df)