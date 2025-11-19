customer = {
    "name":"John",
    "city":"NYC",
    "balance":1000
}
print("*** My Bank ATM ***")
menu = """
1. Deposit
2. Withdraw
3. Exit
"""
while True:
    print(menu)
    ch = input("Enter choice: ")
    match ch:
        case "1":
            amount = int(input("Enter amount: "))
            customer["balance"] = customer["balance"]+amount
            print("Your current balance is", customer['balance'])
        case "2":
            amount = int(input("Enter amount: "))
            if customer["balance"]>amount:
                customer["balance"] = customer["balance"]-amount
            else:
                print("Insufficient Balance")
            print("Your current balance is", customer["balance"])
        case "3":
            break
        case _:
            print("Invalid Choice")
            
    
    



    
