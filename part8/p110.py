import pandas as pd
score = {"Maths":[20,30],"Science":[30,25],"English":[50,10]}
df = pd.DataFrame(score,index=["Term-1","Term-2"])
print(df)
# print(df["Maths"])
