print("----- Student Management System -----")
print("1. Add student")
print("2. Display students")
print("3. Search students")
print("4. Count students")
print("5. Exit")
option = int(input("Enter an option: "))
with open("student.txt", "a") as s:
    s.write("101,Deepika,Java,50000\n")
    s.write("102,Ananya,Python,60000\n")
    s.write("103,Anjali,C++,70000\n")
    s.write("104,Anushka,JavaScript,80000\n")
if option == 1:
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")
    salary = input("Enter salary: ")
    with open("student.txt", "a") as s:
        s.write(id + "," + name + "," + course + "," + salary + "\n")
    print("Student added successfully")
elif option == 2:
    with open("student.txt", "r") as s:
        print(s.read())
elif option == 3:
    name = input("Enter student name to search: ")
    n = False
    with open("student.txt", "r") as s:
        for line in s:
            if name in line:
                print("Student found")
                print(line)
                n = True
    if n == False:
        print("Student not found")
elif option == 4:
    count = 0
    with open("student.txt", "r") as s:
        for line in s:
            count = count + 1
    print(count)
elif option == 5:
    print("Exit")
else:
    print("Invalid")