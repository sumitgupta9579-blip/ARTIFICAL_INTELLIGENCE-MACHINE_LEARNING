a=[]
for i in range(1,6):
    a.append(int(input(f"Enter an marks of {i} subject a student :")))
print(a)
avg=sum(a)/5
print(f"Average marks of a student is {avg}")
print(f"Highest marks of a student {max(a)} Lowest marks of a student {min(a)}")
if(avg>=90):
    print("Grade A")
elif(avg >=75 and avg <=89):
    print("Grade B")
elif(avg>=60 and avg <=74):
    print("Grade C")
else:
    print("Grade D")