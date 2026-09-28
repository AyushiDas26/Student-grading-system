student_grades = {}

def add_student(name , grade):
    student_grades[name]= grade
    print(f"{name} with a grade {grade}")


def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with marks are updated{grade}")
    else:
        print("students not found")


def display_all_student():
    student_grades
    for name, grade in student_grades.items():
        print(f"{name}:{grade}")


def main():
    while True:
        print("\n Student Grades Managment System ")
        print(" 1.Add Student ")
        print("2.Update")
        print("3. View all student")
        print("4. Exit \n")

        choice=int(input("Enter your choice"))

        if choice==1:
            name=input("Enter student name=")
            grade=int(input("Enter student grades= "))
            add_student(name,grade)

        elif choice==2:
            name==input("Enter student name= ")
            grade=int(input("Enter student grades="))
            update_student(name,grade)

        elif choice==4:
            print("closing the program")
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
