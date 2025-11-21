def f1():
    a="Hello"
    if not type(a) == int:
        raise Exception("a must be an integer")
    else:
        print("Success")
    
try:
    f1()
except:
    print("Something went wrong")