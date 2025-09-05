# pandas series: is one dimensional array like object that can hold any datatypes
# it is similar to a column in a table
import pandas as pd
data =[1,2,3,4,5]
data_series = pd.Series(data)
print("Here is the data series:\n", data_series) # you get two column, first coulmn is the index
dict = {"a":1,"b":2,"c":3}
dict_series = pd.Series(dict)
print(dict_series)
data2 = [10,20,30]
index =["a","b","c"]
data_series2 = pd.Series(data2,index=index)
print(data_series2)