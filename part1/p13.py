n=1
while n<=5:
    age=int(input("Enter your age:"))
    n=n+1
    if age<20:
        print("Restricted")
        continue
    name=input("Enter name")  
    print(f"Hello {name}")
    flag=input("Continue(y/n)")
    if flag!="y":
        break
else:
    print("Program completed successfully")

# n=1
# while n<=5:
#     name=input("Enter your name:")
#     print(f"Hello {name}")
#     flag=input("Continue(y/n)")
#     n=n+1
#     if flag!="y":
#         break
# else:
#     print("Program completed successfully")

# while True:
#     name=input("Enter your name:")
#     print(f"Hello {name}")
#     flag=input("Continue(y/n)")
#     if flag!="y":
#         break
    
# n=1
# while n<5:
#     print(n)
#     n=n+1