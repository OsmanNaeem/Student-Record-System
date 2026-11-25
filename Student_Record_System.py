students=[]
def add_student():
    name=input("Enter student name:")
    age=int(input("Enter student age:"))
    marks=float(input("Enter student marks:"))
    student={
        "name":name,
        "age":age,
        "marks":marks
    }
    students.append(student)
    print("Student added successfully!")
def view_students():
    if not students:
        print("No student records found.")
        return
    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
def average_marks():
    if not students:
        print("No student records found.")
        return
    total = 0
    for student in students:
        total = total + student["marks"]
    average = total / len(students)
    print("Average marks:", average)
def show_menu():
    while True:
        print("\n===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Average Marks")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            average_marks()
        elif choice == "4":
            print("Thank you for using Student Record System!")
            break
        else:
            print("Invalid choice! Please select 1-4.")
show_menu()