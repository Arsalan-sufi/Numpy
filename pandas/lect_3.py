import pandas as pd

#hoe to create a dataframe using dictionary
data={
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[10,20,30],
    "City":['Nagpur','Mumbai','Delhi']

}

df=pd.DataFrame(data)
print(df)

#Now saving this file in CSV,EXCEL,JSON--------

#index = false se index[ID] gayab hoti h

#df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
# df.to_json("output.json", index=False)
