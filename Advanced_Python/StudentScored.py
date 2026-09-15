for student in students:
    print(student)

for student in students:
    print(student["name"])


sum=0
for student in students:
    sum+=student["marks"]

print(sum)


sum=0
for student in students:
    sum+=student["marks"]

print(sum/len(students))


passed_count=0
for student in students:
    if(student["marks"]>=40):
        passed_count+=1
print(passed_count)



def grade(marks):
    if(marks>=90):
        print("A")
    elif(marks>=75):
        print("B")
    elif(marks>=60):
        print("C")
    else:
        print("D")

for student in students:
    grade(student["marks"])


roll=int(input("Enter a roll no :"))
search(roll)

def search(roll):
    # found=False
    for student in students:
        if(student["roll"]==roll):
            print(student["name"])
            # found=True
            return "Record Found"
            # break
    return " Not found"


def search(name):
    name=name.lower()
    for student in students:
        if((student["name"]).lower()==name):
            print(student["name"])
            return "Name found"
    return "Not found"



def topper(students):
    marks=0
    for student in students:
        if(student["marks"]>marks):
            marks=student["marks"]

    for student in students:
        if(student["marks"==marks]):
            print("Topper is ",student["name"])


courses={}
for student in students:
    if(student["course"] not in courses):
        courses[student["course"]]=1
    else:
        courses[student["course"]]+=1

print(courses)

course=[]
for student in students:
    courses.append(student["course"])
print(courses)
s=set(courses)
print(s)


class Student():
    def __init__(self,roll,name,course,marks):
        self.roll=roll
        self.name=name
        self.course=course
        self.marks=marks
    def show(self):
        print(self.roll,self.name,self.course,self.marks)

















