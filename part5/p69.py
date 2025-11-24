class employee:
    def __init__(self,name,basicSalary):
        self.n = name
        self.s = basicSalary
    def empDetails(self):
        print(self.n)
    def empSalary(self):
        print(self.s + 2000)
        
e=employee("Srikanth",5000)
e.empDetails()
e.empSalary()
e.s=9000
e.empSalary()