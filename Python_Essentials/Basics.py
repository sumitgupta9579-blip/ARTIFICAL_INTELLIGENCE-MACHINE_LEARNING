# Understanding print() function in python


# print("Hello Dosto !")
# print("Hello ","Dosto !")
# print("A")
# print("B")
# print("C")
# print("Sumit\nGupta")
# print("A",end="#")
# print("B",end="#")
# print("C",end="#")
# print("A",end="#")
# print("B",end="%")
# print("C",end="$")
# print("A",end="\n")
# print("B",end="\n")
# print("C",end="\n")



# Understading variable in python


# variable always start with alphabet(a-z) && (A-Z) or underscore(_)
# And variable name can contain alphabets, numbers(0-9) and underscore(_)
# variable name can not start with number(0-9)


# Understanding data types in python


# a = 10    
# print(a)
# print(type(a))
# b=2.0
# print(type(b))
# c="Sumit Gupta"
# print(type(c))
# d=True  
# print(type(d))
# e='A'
# print(type(e))


# difference between float and double in python
# In python there is no double data type, we use float to represent both single and double precision floating point numbers.


# operators in python

#  1 -> Arithmetic operators

# a=5
# b=2
# print(a+b)  # addition
# print(a-b)  # subtraction
# print(a*b)  # multiplication
# print(a/b)  # division
# print(a//b) # floor division
# print(a%b)  # modulus
# print(a**b) # exponentiation

# 2 ->Comparison operators
# a=5
# b=2
# print(a==b)  # equal to
# print(a!=b)  # not equal to
# print(a> b)  # greater than
# print(a< b)  # less than
# print(a>=b)  # greater than or equal to
# print(a<=b)  # less than or equal to

# print()

# print(a is b)  #  3 ->identity operator
# print(a is not b)  #  4 ->identity operator

# print()

# print(a in [1,2,3,4,5])  #  5->membership operator
# print(a not in [1,2,3,4,5])  # membership operator

# print()

# print(a and b)  # 6--> logical operator
# print(a or b)  # logical operator
# print(not a)  # logical operator
# print(not b)  # logical operator

# print()

# print(a & b)  #  7 -->bitwise operator
# print(a | b)  # bitwise operator
# print(a ^ b)  # bitwise operator
# print(a << 1)  # bitwise operator
# print(a >> 1)  # bitwise operator

# print() 

# print(a)  # -->assignment operator
# a += 1  # assignment operator
# print(a)
# print(a)  # assignment operator
# a -= 1  # assignment operator
# print(a)
# print(a)  # assignment operator
# print(a)  # assignment operator
# a *= 2  # assignment operator
# print(a)
# print(a)  # assignment operator
# a /= 2  # assignment operator
# print(a)
# print(a)  # assignment operator
# a //= 2  # assignment operator
# print(a)
# print(a)  # assignment operator
# a %= 2  # assignment operator
# print(a)
# print(a)  # assignment operator
# a **= 2  # assignment operator
# print(a)


# # if else statement in python
# if a > b:
#     print("a is greater than b")

# if a < b:
#     print("a is less than b")
# else:
#     print("a is greater than b")


# if a == b:
#     print("a is equal to b")
# elif a != b:
#     print("a is not equal to b")
# else:
#     print("a is equal to b")



# for loop in python


# for i in range(1,11):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)


# while loop in python


# i=1
# while i<=10:
#     print(i)
#     i+=1

# while i>=1:
#     print(i)
#     i-=1        

# a=1
# while a<=10:
#     print(a)
#     a+=1

# function in python


# def add(a,b):
#     return a+b  

# def sub(a,b):
#     return a-b
# def greet(name):
#     print("Hello "+name)


# Taking input from user in python

# name = input("Enter Your Name : ")
# print("Hello "+name)

# a = int(input("Enter First Number : "))
# b = int(input("Enter Second Number : "))
# if(a>b):
#     print("First Number is Greater than Second Number")
# elif(a<b):
#     print("Second Number is Greater than First Number")
# else:
#     print("Both Numbers are Equal")



# year = int(input("Enter Year : "))
# age = int(2026-year)
# print("Your Age is : "+ str(age))



# Method 1: If you only know the birth year


# from datetime import date

# birth_year = int(input("Enter Year : "))
# current_year = date.today().year

# age = current_year - birth_year

# print(age)



# x = float(input("Enter length of rectangle :"))
# y = float(input("Enter breadth of rectangle :"))
# area = x*y
# print("Area of rectangle is : "+str(area))



# name = input("Enter Your Name : ")
# age = int(input("Enter Your Age : "))
# height = float(input("Enter Your Height : "))   

# print("Your Name is : "+name , "Your Age is : "+str(age) , "Your Height is : "+str(height))

 