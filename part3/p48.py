import random
print("*** Math Quiz ***")
op = ["+","-","/","*"]
score=0
for i in range(1,6):
    n1 = random.randint(10,99)
    n2 = random.randint(1,9)
    q = f"{n1}{random.choice(op)}{n2}"
    print(f"{i}.{q}=",end="")
    answer = int(input())
    if answer == eval(q):
        score=score+1
        print("Correct")
    else:
        print("Better luck next time")
print("Your score is",score)
    
