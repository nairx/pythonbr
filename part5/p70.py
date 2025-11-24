class employee:
    def __init__(self,name):
        self.n=name
    def empDetails(self):
        print(self.n)
        
class consultant(employee):
    def __init__(self,name,msg):
        super().__init__(name)
        self.msg = msg
    def greet(self):
        print(self.msg)
           
c = consultant("Pratap","Hello World")
c.empDetails()
c.greet()



