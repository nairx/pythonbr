customer = {
    "name":"John",
    "city":"NYC",
}
# print(customer["city"])
# print(customer["balance"])
# print(customer.get("balance"))
# print(customer.get("balance",0))
# customer["balance"] = 1000
# customer["balance"] = 3000
# customer["balance"] = customer["balance"] + 3000
# customer["balance"] = customer.get("balance")+2500
customer["balance"] = customer.get("balance",0)+2500
print(customer)