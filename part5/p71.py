class parent:
    def method1(self):
        print("method 1")

class child(parent):
    def method2(self):
        print("method 2")
    def method1(self):
        print("method 1 of child")

c = child()
c.method2()
c.method1()


