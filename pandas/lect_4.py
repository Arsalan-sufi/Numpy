##Before manipulating dataset we neet to ask two questions to ourselves
"""
1- how big is our datset
2-what are the names of the columns
3-shape and columns(returns tupple)
"""


import pandas as pd

data={
    "Name":['ram','ghanshyam','lolo','aditi','arsalan','raj','roman'],
    "Age":[23,43,21,45,78,54,33],
    "Salary":[5000,242342,56666,65432,89797,22222,224455],
    "Performance Score":[85,90,77,68,87,53,54]
}
df=pd.DataFrame(data)

print(f'Shape:{df.shape}')
print(f'Column Names:{df.columns}')

