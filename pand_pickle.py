# picckle in python is the process of converting a python object into a byte stream 
# to store it in a file / database , mainatain program state across session or transport data 
# overthe net work.
import pandas as pd
df_xl = pd.read_excel("xl_data.xlsx")
#print(df)
df_xl.to_pickle("df_pickle")#it will create a bite stream file,'df_pickle', in local; which can not read. 