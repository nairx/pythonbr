import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Year": ["2020", "2021", "2022", "2023"],
    "Sales": [150, 100, 550, 300]
}
df = pd.DataFrame(data)
df.plot(x="Year",y="Sales")
plt.show()
# print(df)