def f2(f):
    def wrapper():
         print("function f1 starts")
         f()
         print("function f1 ends")
    return wrapper

@f2
def f1():
    print("I am function f1")
    
f1()