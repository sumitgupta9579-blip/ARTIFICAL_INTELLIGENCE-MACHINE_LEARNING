sub1 = []
sub2 = []

for i in range(5):
    sub1.append(input("Enter first student subject: "))
    sub2.append(input("Enter second student subject: "))

print("Subjects of student 1:", sub1)
print("Subjects of student 2:", sub2)

common = set(sub1).intersection(set(sub2))

print("Common subjects:", common)