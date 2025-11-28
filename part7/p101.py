import matplotlib.pyplot as plt
x = ["2021","2022","2023","2024","2025"]
y = [10,23,45,51,50]
plt.plot(x,y,color='green',linestyle="--",marker="x",label='Sales')
plt.title("Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales(Cr)")
plt.legend()
plt.savefig("./part7/report.jpg")
plt.show()

