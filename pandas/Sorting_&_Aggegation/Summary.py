"""
df["COl Name"].mean()
df["COl Name"].min()
df["COl Name"].max()
df["COl Name"].sum()

"""


import pandas as pd

data={
    "Name":['Arum','Yawer','Karan'],
    "Age":[28,25,58],
    "Salary":[10000,20000,40000]
}

df=pd.DataFrame(data)

avg_salary=df['Salary'].mean()
print(avg_salary)