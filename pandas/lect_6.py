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
##Now let`s see what describe method does:
print("Descriptibe Statistics")
print(df.describe())
 