import pandas as pd
# Dataframe are two dimentional with multiple rows and columns 
# Dictionary of lists
data = {
    "name":["Chris", "Raja", "John"," George"],
    "age":[38,27,32,45],
    "city":["Berlin","Kottayam","Toronto","Munich"]
}
df = pd.DataFrame(data)
#print(df)
# list of dictioneries
data2 = [ 
         {"name":"Chris", "age": 38, "city":"Berlin"},
         {"name":"Raja", "age": 27, "city":"Kottayam"},
         {"name":"John", "age": 32, "city":"Toronto"},
         {"name":"George", "age": 45, "city":"Munich"}
]
df2 = pd.DataFrame(data2)
#print(df2)
print(df2["name"])
#print(df2.iloc[0]) # location index 0 means entire row of 0 index
#print(df2.iloc[0][0]) # first row 0 and 0 column that is Chris 
#print(df2.iloc[0][2]) # first row 0 and 2 column that is Berlin 

# print(df2.at[1,"age"]) # row one Age is 27
# print(df2.at[2,"name"]) # row two name is John
#print(df2.iat[1,1]) # row one column 1 is 27