import pandas as pd
score = [45,50,60]
# series = pd.Series(score)
# print(series)
# print(series[0])
series = pd.Series(score,index=["Maths","Science","English"])
print(series)
print(series["Maths"])