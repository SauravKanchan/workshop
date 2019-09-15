class Person():
    def __init__(self,first_name, last_name):
        print("Hello",first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name

    def say_hi(self):
        print("Hi",self.first_name)

    def set_name(self,fn,ln):
        self.first_name = fn
        self.last_name = ln

    def get_name(self):
        return self.first_name+" "+self.last_name

person = Person("Saurav","Kanchan")
# person.say_hi()
# person.set_name("Jhon","Doe")
# person.say_hi()
print(person.get_name())