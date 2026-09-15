
# List are immutable we can changed the data

days=["Monday","Tuesday","Wednesday","Thrusday","Ftiday","Saturday","Sunday"]
days[0]="SG DAY"
# print(days)


# Tuples are immutable we cant change data in a list

days=("Monday","Tuesday","Wednesday","Thrusday","Ftiday","Saturday","Sunday")
# days[0]="SG DAY"
# print(days)

c=(1)
print(type(c))

d=(1,)
print(type(d))
print(len(d))

a=("SG",9.9,24,True)
for ele in a:
    print(ele)

n=len(a)
for i in range(n):
    print(a[i])

print(a[1:3])

b=("p","q","r")
print("a"in b)

b=("p","q","r")
print("a" not in b)

num=(2,4,5)
print(sum(num))

print(num.count(4))

print(num.index(5))

student=("Raj",9.9,24)
type(student)

# unpacking
name,cgpa,age=student
print(name)
print(cgpa)
print(age)

name,cgpa,age=("raj",9.9,24)
print(name ,age,cgpa)