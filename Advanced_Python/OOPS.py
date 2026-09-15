#  Class is a blueprint 
#  object is specific instance of that class

#  e.g: Class -> Car
#       Object->Volvo,BMW,Suzuki

#  Class

# class ClassName:
#     x=10
#  Object created

# p1=ClassName()
# print(p1.x)

# p2=ClassName()
# print(p2.x)

# p3=ClassName()
# print(p3.x)


# class car:
#     no_Of_wheels=4

# c1=car()
# print(c1.no_Of_wheels)

# c2=car()
# print(c2.no_Of_wheels)

# class person:
#     name="raj"
#     city="Mumbai"
#     age=18
#     height=6.8
#     weight=50

# p1=person()
# print(p1.name ,p1.age)

# p2=person()
# print(p2.height,p2.weight)

# p3=person()
# print(p3.city)

# __init__()

#  it is a built in method which is always exceuted when the class get intiataed or object is being created


# class person:
#     def __init__(self,name,city):
#         self.name=name
#         self.city=city
# p1=person("Raj","Mumbai")
# print(p1.name,p1.city)

# p2=person("Sumit","UP")
# print(p2.name,p2.city)


# class student:
    # pass 
    # placeholder- > do nothing

class Student:
    name="Raj"
    age="21"
    city="Mumbai"

s1=Student()
# print(s1.name,s1.age,s1.city)

class Class:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display_profile(self):
        print(self.name,self.city,self.age)

c1=Class("Sumit",20,"Mumbai")
# print(c1.name,c1.city,c1.age)
c2=Class("Pravin",25,"Kamote")
# print(c2.name,c2.city,c2.age)
c3=Class("Swapnil",54,"Khopoli")
# print(c3.name,c3.city,c3.age)
c4=Class("Sahil",15,"Pune")
# print(c4.name,c4.city,c4.age)
c1.display_profile()
c2.display_profile() 







