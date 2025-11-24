from abc import ABC,abstractmethod
class user(ABC):
    @abstractmethod
    def details(self):
        pass
    @abstractmethod
    def salary(self):
        pass
class employee(user):
    def details(self):
        print("Employee Details")
    def salary(self):
        print("employee class salary method")
class student(user):
    def details(self):
        print("Student Details")
    def salary(self):
        print("student class salary method")
e = employee()
e.details()
s = student()
s.details()
s.salary()

