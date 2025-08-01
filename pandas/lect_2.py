#how to see rows --- understand the structure of data first 
#head() returns the first few rows of a DataFrame (default is 5), while tail() returns the last few rows.

import pandas as pd

df=pd.read_json("sample_Data.json")

print('display 10 rows of first')
print(df.head(10))

print('display 10 rows of last')
print(df.tail(10))
 