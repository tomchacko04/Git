import pandas as pd
url ="https://www.fdic.gov/bank-failures/failed-bank-list"
df = pd.read_html(url)
# print(df)
url2 = "https://en.wikipedia.org/wiki/Mobile_country_code"
df2 = pd.read_html(url2,match="Country",header=0)
print(df2)