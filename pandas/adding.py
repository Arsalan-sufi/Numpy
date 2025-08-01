import pandas as pd

data={
    "Name":['ram','ghanshyam','lolo','aditi','arsalan','raj','roman'],
    "Age":[23,43,21,45,78,54,33],
    "Salary":[5000,242342,56666,65432,89797,22222,224455],
    "Performance Score":[85,90,77,68,87,53,54]
}
df=pd.DataFrame(data)

print("Sample Dataframe")
print(df)


#This will create a column at last
df['bonus']=df["Salary"]*0.1
print(df)

#now let's see how can we create column at rondom position
#Syntax: df.insert(Loction,"Column Name",data)
df.insert(0,'Employee id',[1,2,3,4,5,6,7])
print(df)