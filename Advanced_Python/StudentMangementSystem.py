students = []


class Student:
    def __init__(self, name, roll, age, course, marks):
        self.name = name
        self.roll = roll
        self.age = age
        self.course = course
        self.marks = marks


def add_student():
    name = input("Enter Student Name : ")
    roll = int(input("Enter Roll Number : "))
    age = int(input("Enter Age : "))
    course = input("Enter Course : ")
    marks = float(input("Enter Marks : "))

    s = Student(name, roll, age, course, marks)
    students.append(s)

    print("Student Added Successfully.")


def display_students():
    if len(students) == 0:
        print("No Student Records Found.")
        return

    print("\n------ Student Records ------")
    for s in students:
        print("Name   :", s.name)
        print("Roll   :", s.roll)
        print("Age    :", s.age)
        print("Course :", s.course)
        print("Marks  :", s.marks)
        print("-----------------------------")


def search_student():
    roll = int(input("Enter Roll Number to Search : "))

    for s in students:
        if s.roll == roll:
            print("\nStudent Found")
            print("Name   :", s.name)
            print("Roll   :", s.roll)
            print("Age    :", s.age)
            print("Course :", s.course)
            print("Marks  :", s.marks)
            return

    print("Student Not Found.")


def find_topper():
    if len(students) == 0:
        print("No Student Records.")
        return

    topper = students[0]

    for s in students:
        if s.marks > topper.marks:
            topper = s

    print("\nTopper Details")
    print("Name :", topper.name)
    print("Roll :", topper.roll)
    print("Marks:", topper.marks)


def calculate_average():
    if len(students) == 0:
        print("No Student Records.")
        return

    total = 0

    for s in students:
        total += s.marks

    average = total / len(students)

    print("Average Marks =", average)


def save_file():
    file = open("students.txt", "w")

    for s in students:
        file.write(f"{s.name},{s.roll},{s.age},{s.course},{s.marks}\n")

    file.close()

    print("Data Saved Successfully in students.txt")


while True:

    print("\n====== Student Management Menu ======")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Calculate Average")
    print("6. Save File")
    print("7. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        find_topper()

    elif choice == 5:
        calculate_average()

    elif choice == 6:
        save_file()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")