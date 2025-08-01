import pandas as pd

data={
    "Name":['ram','ghanshyam','lolo','aditi','arsalan','raj','roman'],
    "Age":[23,None,21,45,78,54,33],
    "Salary":[70000,None,56666,65432,89797,22222,224455],
    "Performance Score":[None,90,77,68,87,53,54]
}
df=pd.DataFrame(data)

print("Sample Dataframe")
print(df)
print("\n")

#interpolarion types: Linear, polynomial, time etc
#Because linear interpolation requires at least one previous and one next valid number to calculate the interpolated value.
df.interpolate(Method="linear", axis=0, inplace=True)
print(df)