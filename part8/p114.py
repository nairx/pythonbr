import pandas as pd
df = pd.read_csv("./part8/student.csv")
# print(df)
# print(df.head(1))
# print(df.tail(1))
# print(df.info())
newdf = df.dropna()
print(newdf)