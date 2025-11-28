import pandas as pd
score = {
    "subjects":["Maths","Science","English"],
    "marks":[45,50,40]
}
df = pd.DataFrame(score,index=["Day-1","Day-2","Day-3"])
df.to_csv("./part8/test.csv",index=False)
print(df)
print(df.loc["Day-1"])