#Vertically
import pandas as pd

df_region1=pd.DataFrame({
    "CustomerID": [1,2],
    "Name": ["Raju","Shaam"]
})

df_region2=pd.DataFrame({
    "CustomerID": [3,4],
    "Name": ["Babubhai","Anuradha"]
})

df_concat=pd.concat([df_region1,df_region2],axis=0,ignore_index=True)
print(df_concat)