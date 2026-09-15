# try:
#         a=int(input("Enter first number :"))
#         b=int(input("Enter second number :"))
#         print("The division of two numbers is : ",a/b)
# except Exception as e:
#         print(e)


# try:
#         a=int(input("Enter first number :"))
#         b=int(input("Enter second number :"))
#         print("The division of two numbers is : ",a/b)
# except ZeroDivisionError:
#         print("Division by 0 is not allowed")

# except ValueError:
#         print("Please emter numbers only")


# try:
#         a=int(input("Enter first number :"))
#         # b=int(input("Enter second number :"))
#         # print("The division of two numbers is : ",a/b)
#         print(100/a)
#         n=[3,6]
#         print(n[4])

# except ZeroDivisionError:
#         print("Division by 0 is not allowed")

# except ValueError:
#         print("Please emter numbers only")

# except Exception as e:
#         print("Some error has occured")


# try:
#         num=int(input("Enter first number :"))
        
# except ValueError:
#         print("Invalid Input")

# else:
#         print("You entered:",num)


# Finally block always execute irrespective whether there is an error or not

try:
        num=int(input("Enter first number :"))
        
except ValueError:
        print("Invalid Input")

finally:
        print("Program finished ")