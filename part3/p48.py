import random
print("*** Math Quiz ***")
op = ["+","-","/","*"]
for i in range(1,6):
    n1 = random.randint(10,99)
    n2 = random.randint(1,9)
    print(f"{i}.{n1}+{n2}=",end="")
    answer = int(input())
    if answer == n1+n2:
        print("Correct")
    else:
        print("Better luck next time")
    
    
