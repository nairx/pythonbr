class employee:
    def __init__(self,name):
        self.__n = name
    def setName(self,name):
        self.__n = name
    def getName(self):
        return self.__n
        

e = employee("John")
print(e.getName())
e.setName("Cathy")
print(e.getName())

