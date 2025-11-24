from abc import ABC,abstractmethod
class user(ABC):
    @abstractmethod
    def empDetails(self):
        pass

class employee(user):
    def __init__(self,name):
        self.__n = name
    def empDetails(self):
        print(self.__n)
    def setName(self,name):
        self.__n = name
        
    

e = employee("John")
e.empDetails()
e.setName("Amy")
e.empDetails()

#update the name
#print the name