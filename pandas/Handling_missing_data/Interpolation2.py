import pandas as pd

data={
    "Time":[1,2,3,4,5],
    "Value":[10,None,50,None,120]
}
df=pd.DataFrame(data)
print('Before interpolation')
print(df)
print("\n")


print("After interpolation")

df["Value"]=df["Value"].interpolate(method="linear")
print(df)

"""When to use interpolation
1-time series data
2-numeric data with trends
3-avoid dropping rows
"""