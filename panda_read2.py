import pandas as pd
df = pd.read_csv("sales_data.csv")# df means dataframe 
#print(df)
#print(df.head(2)) # gives two recods from head
df["New_Value"] = df["Value"].astype(float) #it will give a new column with data_type float column name: Age_new 
#print(df)
df["New_Value"] = df["Value"].fillna(df["Value"].mean()).astype(int)#it will give a new column with data_type int column name: Age_new 
#print(df)
df["New_Value"] = df["Value"].apply(lambda x:x*2) 
print(df)