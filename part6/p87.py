from time import sleep
import threading
def f1():
    for i in range(5):
        print("This is f1 function")
        sleep(3)
    
def f2():
    for i in range(5):
        print("This is f2 function")
        sleep(2)
    
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Program Completed Successfully")
