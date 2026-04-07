students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added!")

def view_students():
    if not students:
        print("No students found.")
    else:
        for i, s in enumerate(students, 1):
            print(f"{i}. {s}")

def delete_student():
    view_students()
    num = int(input("Enter number to delete: "))
    if 0 < num <= len(students):
        students.pop(num-1)
        print("Deleted!")
    else:
        print("Invalid choice")

while True:
    print("\n1. Add Student\n2. View Students\n3. Delete Student\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice")