import pandas as pd
#df = pd.read_csv("mysample.csv")
df = pd.read_csv("sales_data.csv")
#print(df)
#print(df.head(3)) # top first 3
#print(df.tail(3)) # bottom last 3
#print("Statistical summary\n", df.describe())
#print(df.dtypes)# object means strings int64 means intger, if there is float column it will say so.
#print(df.isnull()) # if any column has missing values it will say true
#print(df.isnull().any()) # meaning all name coulmn has no missing value etc
#print(df.isnull().sum()) # how many miising values sum toatl eg: in coulmn 2, there area 3 values are missing
#print(df.fillna(0)) # whereever there is null value fill with 0
#["Age_fill"] = df["Age"].fillna(df["Age"].mean())
df = df["Sales"].fillna(df["Sales"].mean())
print(df)
