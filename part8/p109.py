import pandas as pd
score = {"Maths":45,"Science":50,"English":75}
# series = pd.Series(score)
# print(series)
series = pd.Series(score,index=["Maths","Science"])
print(series)