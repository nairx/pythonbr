import matplotlib.pyplot as plt
x = ["2021","2022","2023","2024","2025"]
y = [10,23,45,51,50]
z = [12,20,50,30,90]
plt.plot(x,y,color='green',linestyle="--",marker="x",label='iPhone')
plt.plot(x,z,color='blue',linestyle="--",marker="x",label='Oneplus')
plt.title("Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales(Cr)")
plt.legend()
plt.savefig("./part7/report.jpg")
plt.show()