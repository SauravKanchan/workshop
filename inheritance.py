class Person():
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_name(self,fn,ln):
        self.first_name = fn
        self.last_name = ln

    def get_name(self):
        return self.first_name+" "+self.last_name

class Student(Person):
    def set_roll_no(self, number):
        self.roll_no = number
        print(self.roll_no)

    def get_name(self):
        super()
        print(self.first_name+" "+self.last_name)

student1 = Student("Jhon","Doe")
student1.set_roll_no(23)
student1.get_name()
student1.roll_no = 34
print(student1.roll_no)