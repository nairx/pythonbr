# name = "Vamsi"
# location = "Hyderabad"

emp1 = {
    "name":"Vamsi",
    "location":"Hyderabad",
    "phone":"34534355"
}
# print(emp1)
# print(emp1["name"])
# print(emp1.values())
# print(emp1.keys())
# print(emp1.items())
# for i in emp1.keys():
#     print(i)
# for i in emp1.values():
#     print(i)
# for i in emp1.items():
#     print(i)
# for i,j in emp1.items():
#     print(i,j)

emp1["phone"] = "123456"
print(emp1)
emp1["department"]="IT"
print(emp1)
del emp1["location"]
print(emp1)