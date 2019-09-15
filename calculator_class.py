class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a+self.b)

    def addtion2(self,a,b):
        print("first defication")
        print(a+b)

    def addtion2(self, a,b,c):
        print("second defination")
        print(a+b+c)

compute = Calculator(3,4)
compute.addition()
# compute.addtion2(5,6)
compute.addtion2(5,6,4)