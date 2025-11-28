import matplotlib.pyplot as plt
x = ["2021","2022","2023","2024","2025"]
y = [10,23,45,51,50]
plt.scatter(x,y,color="green")
plt.title("Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales(Cr)")
plt.legend()
# plt.grid(True,color="grey")
plt.savefig("./part7/report.jpg")
plt.show()