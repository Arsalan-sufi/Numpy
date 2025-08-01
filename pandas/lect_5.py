import pandas as pd

data={
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[10,20,30],
    "City":['Nagpur','Mumbai','Delhi']

}
#Small data set
# df=pd.DataFrame(data)
# print('Displaying the info of data set')
# print(df.info())

#Larger data set
df=pd.read_json("sample_Data.json")
print('Displaying the info of data set')
print(df.info())
