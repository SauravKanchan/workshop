class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a+self.b)

compute = Calculator(3,4)
compute.addition()