##Targeting multiple columns:

import pandas as pd

data={
    "Name":['ram','ghanshyam','lolo','aditi','arsalan','raj','roman'],
    "Age":[23,43,23,45,78,54,33],
    "Salary":[5000,242342,56666,65432,89797,22222,224455],
    "Performance Score":[85,90,77,68,87,53,54]
}

#First sort by "Age" ascending.
# Then within the same Age, sort by "Salary" descending.
df=pd.DataFrame(data)
df.sort_values(by=["Age","Salary"],ascending=[True,False], inplace=True)
print("Sorted Age by ascending")
print(df)


