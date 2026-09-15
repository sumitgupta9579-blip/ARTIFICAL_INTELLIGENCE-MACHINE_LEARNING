
# # File handling is for creating , reading and deleting a file

# file.open()   (open the ifle it will also create a new file)
# file.write    (write  "w")
# file.read     (read "r")
# file.append   (add "a")
# file.close()  (close the file after doing work)

# # Most commmonly used types of files in AIML --> text , csv


# # csv -> comma seperated values .

# #  Ex - Name , Marks , City
# #       Rahul , 95 , Nagpur


# # syntax 
# # file = open(filename , mode)

# file = open("demo.txt","w")
# file.write("Sahil Barnekar \n")
# file.write("Pravin Kale \n")
# file.write("Swapnil date \n")
# file.close()

# file = open("demo.txt","r")
# data = file.read()
# print(data)
# file.close()

# file = open("demo.txt","r")
# data = file.readline()
# print(data)
# file.close()

# file = open("demo.txt","r")
# data = file.readlines()
# print(data)
# file.close()

# for line in data :
#     print(line)

# file = open("demo.txt" ,"r")
# for line in file:
#     print(line)
# file.close()


# write("w") code will create and replace but append ("a") will add 

# file = open("demo.txt","a")
# file.write("Aditya Jain \n")
# file.close()

# file = open("demo.txt","r")
# data=file.read()
# file.close()
# print(data)


# file = open("abc.txt","x")
# file.close()

# with open("demo.txt","r") as file:
#     print(file.read())

with open("demo.txt","w") as file:
    file.write("Hello Everyone !")

# with open("demo.txt","r") as file:
#     print(file.read())

with open("demo.txt","a") as file:
    file.write("\nSumit Gupta here this side ..........")

with open("demo.txt","r") as file:
    print(file.read())

