from time import sleep
import threading

def f1(x):
    for i in range(5):
        print(f"Value of x is {x}")
        sleep(3)
    
def f2(y):
    for i in range(5):
        print(f"Value of y is {y}")
        sleep(2)
    
t1 = threading.Thread(target=f1,args=(3,))
t2 = threading.Thread(target=f2,args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Program Completed Successfully")
