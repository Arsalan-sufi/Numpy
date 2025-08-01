#It is like Joins in SQL
#Syntax:
#pd.merge(df1, df2,  on='Col Name', how="type"of join)

import pandas as pd 

#Customer dataframe
df_customers=pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":['Arsalan','Saheem','Saliq']
})

df_orders=pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[230,211,400]
})

df = pd.merge(df_customers, df_orders, on='CustomerID', how = 'inner')
print(df)

df = pd.merge(df_customers, df_orders, on='CustomerID', how = 'left')
print(df)

df = pd.merge(df_customers, df_orders, on='CustomerID', how = 'right')
print(df)

df = pd.merge(df_customers, df_orders, on='CustomerID', how = 'outer')
print(df)