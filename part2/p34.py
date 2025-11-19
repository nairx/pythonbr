customers = []
print("*** My Bank ***")
while True:
    print("1.New Customer\n2.Existing Customer\n3.Exit")
    ch = input("Enter your choice: ")
    if ch=="1":
        card = input("Enter card#")
        pin = input("Enter pin")
        name = input("Enter name")
        balance = int(input("Enter balance"))
        customers.append({"card":card,"pin":pin,"name":name,"balance":balance})
        print(customers)
    elif ch=="2":
        card = input("Enter card#")
        pin = input("Enter pin")
        for i in range(len(customers)):
            if customers[i]["card"] == card and customers[i]["pin"] == pin:
                menu = """
                1. Deposit
                2. Withdraw
                3. Exit
                """
                customer={}
                while True:
                    print(menu)
                    ch = input("Enter choice: ")
                    match ch:
                        case "1":
                            amount = int(input("Enter amount: "))
                            customers[i]["balance"] = customers[i]["balance"]+amount
                            print("Your current balance is", customers[i]["balance"])
                        case "2":
                            amount = int(input("Enter amount: "))
                            if customer["balance"]>amount:
                                customers[i]["balance"] = customers[i]["balance"]-amount
                            else:
                                print("Insufficient Balance")
                            print("Your current balance is", customers[i]["balance"])
                        case "3":
                            break
                        case _:
                            print("Invalid Choice")
    elif ch=="3":
        break