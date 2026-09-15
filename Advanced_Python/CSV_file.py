import csv
with open("student.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Marks","City"])
    writer.writerow(["Raj","90","Mumbai"])
    writer.writerow(["Rahul","85","Nagpur"])
    writer.writerow(["Sumit Gupta","98","Kolkata"])

# with open("student.csv","r",newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# take a new record as input from the user and add to file
name = input()
marks = int(input())
city = input()

with open("student.csv","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name,marks,city])

with open("student.csv","r",newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)