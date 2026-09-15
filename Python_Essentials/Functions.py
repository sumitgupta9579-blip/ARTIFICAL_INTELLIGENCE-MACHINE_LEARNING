def greet():
    print("Hello")
# greet()


# name=input("Enter your name : ")
def call(name):
    print("Hello", name)
# call(name)

def show(name,age):
    print("Hello Your name is :",name)
    print("Your age is :",age)
# show("Raj",18)
# show(30,"Gupta")


# KEYWORD ARGUMENT
# show(name="Sumit",age=20)


# RETURN KEYWORD
def sum(a,b):
    return a+b
s=sum(2,3)
print(s)
print(sum(5,8))