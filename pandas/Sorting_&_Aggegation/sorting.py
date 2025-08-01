#Sorting data
#Sorting data in 1 column :sort_values()

# df.sort_values(by="Column Name", True/False , inplace=True)----True/False here denotes acending order=True , decending ordre=False

import pandas as pd

data={
    "Name":['ram','ghanshyam','lolo','aditi','arsalan','raj','roman'],
    "Age":[23,43,21,45,78,54,33],
    "Salary":[5000,242342,56666,65432,89797,22222,224455],
    "Performance Score":[85,90,77,68,87,53,54]
}
df=pd.DataFrame(data)
df.sort_values(by="Age",ascending=True, inplace=True)# it will not just sort the age but also all all the rows like if age belongs to lolo then as per ascending order of age lolo will be placed up or down
print("Sorted Age by ascending")
print(df)


