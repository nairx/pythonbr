def companyName(f):
    def wrapper():
        print("Broadridge")
        f()
    return wrapper

@companyName
def studentName():
    print("Lasya")
   
studentName()