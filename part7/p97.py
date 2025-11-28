from collections import UserString
class MyString(UserString):
    def upper(self):
        return self.data.lower()
name = MyString("jOhn")
print(name.upper())
print(name.title())

