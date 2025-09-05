#data aggregation and grouping with pandas
import  pandas as pd
df = pd.read_csv("sales_data.csv")
grouped_mean = df.groupby("Product")
#print(grouped_mean)# no result
grouped_mean = df.groupby("Product")["Value"].mean()
#print(grouped_mean)
grouped_sum = df.groupby(["Product","Region"])["Value"].sum()
#print(grouped_sum)
grouped_mean2 = df.groupby(["Product","Region"])["Value"].mean()
#print(grouped_mean2)
grouped_agg = df.groupby("Region")["Value"].agg(["mean","sum", "count"])
print(grouped_agg)