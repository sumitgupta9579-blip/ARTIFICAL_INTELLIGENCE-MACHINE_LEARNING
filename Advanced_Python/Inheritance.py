# Parent class -> The class we are inherting from -> base class
# Child class -> The class that inherits from another class -> derived class

class Person:
    def __init__(self ,name , lastname):
        self.name=name
        self.lastname=lastname

    def show_name(self):
        print(self.name,self.lastname)

p1=Person("Raj " , "Sharma")
p1.show_name()

class Student(Person):
    pass
s1=Student("Raj","Sharma")
s1.show_name()

