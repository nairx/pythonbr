import pandas as pd
df = pd.read_csv("./part8/student.csv")
# df["Science"].fillna(120,inplace=True)
# x = df["Science"].mean()
# x = df["Science"].median()
x = df["Science"].mode()
df["Science"].fillna(x,inplace=True)
print(df)