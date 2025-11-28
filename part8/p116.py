import pandas as pd
df = pd.read_csv("./part8/student.csv")
print(df)
df["doj"]=pd.to_datetime(df["doj"])
print(df)