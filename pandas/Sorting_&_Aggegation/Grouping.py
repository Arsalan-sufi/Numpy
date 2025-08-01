"""
Some common aggregation functions:
1-sum()
2-mean()
3-max()
4-min()
5-count()
6-sd()   ---[standard deviation]

"""

import pandas as pd

data={
    "Name":['Arum','Yawer','Karan','Varun','Marun'],
    "Age":[28,25,28,42,42],
    "Salary":[50000,20000,40000,60000,45678]

}

df = pd.DataFrame(data)

#Group + Aggregation
grouped=df.groupby('Age')["Salary"].sum()
print(grouped)

""""
what exactly this method does:

df.groupby("Age")
age = 28 --- [50000,40000]
age = 25 --- [20000]
age = 42 --- [60000,45678]

['Salary].sum()
age = 28 --- [50000,40000] = 90000
age = 25 --- [20000] = 20000
age = 42 --- [60000,45678] = 105678

"""
##For multiple columns its simple just pass as lift 
#Syntax:

data={
    "Name":['Arum','Yawer','Karan','Varun','Marun'],
    "Age":[28,25,28,42,42],
    "Salary":[50000,20000,40000,60000,45678]

}

df = pd.DataFrame(data)

#Group + Aggregation
grouped=df.groupby(['Age','Name'])["Salary"].sum()
print(grouped)
