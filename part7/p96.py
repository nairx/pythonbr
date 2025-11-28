from collections import UserList
class MyList(UserList):
    def pop(self,s=None):
        raise Exception("Pop not allowed")

list = MyList(["John","Amy","Cathy"])
list.pop()
print(list)




