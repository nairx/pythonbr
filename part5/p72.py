class emp:
    def empDetails(self,name,age=None,city=None):
        if age==None and city==None:
            print(name)
        elif city==None:
            print(name,age)
        elif age == None:
            print(name,city)
        else:
            print(name,age,city)

e = emp()
e.empDetails("Sanat")
e.empDetails("Sanat",27)
e.empDetails("Sanat",27,"Bengluru")