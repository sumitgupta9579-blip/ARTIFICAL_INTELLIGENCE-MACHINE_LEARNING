students =["Rahul","Amit","Rahul","Neha","Amit","Rahul"]
# print(students)

s1 =[]
for student in students:
    if student not in s1:
        s1.append(student)

# print(s1)


num ={3,6,8,2,1}
# print(type(num))

fruits = {"Apple","Banana","Orange"}
# print(len(fruits))


num ={4,5,7,2,4,8,1}
# print(len(num))

s={4,5.5,"AJ",False}
# print(type(s))

l=[]
print(type(l))
t=()
print(type(t))
d={}
print(type(d))
s=set()
print(type(s))

num={8,5,7,4,12,4,6}
print(num)
# for n in num:
    # print(n)

num.add(10)
print(num)

num.remove(4)
print(num)

item=num.pop()
print(item)

num.clear()
print(num)


