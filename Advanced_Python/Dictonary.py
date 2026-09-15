student = {
    "name": "Rahul",
    "age": 22,
    "CGPA": 9.5,
    "City": "Nagpur",
}

# print(student)
# print(type(student))

# print(student["name"])
# print(student["CGPA"])
# student["age"]=25
# print(student['age'])
# student["state"]="Maharashtra"
# print(student)
# print(student.get("age"))
# print(student.get("address"))
# print(student.get("address","Key not found"))
# print(student.get("age","Key not found"))
# print(student.pop("state"))
# print(student)

for k in student.keys():
    print(k)

for k in student.keys():
    print(student[k])

# for k in student.values():
#     print(k)

for ele in student.items():
    print(ele)