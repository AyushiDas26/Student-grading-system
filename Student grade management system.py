student_grades = {}

def add_student(name , grade):
    student_grades[name]= grade
    print(f"{name} added with a grade {grade}")


def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} marks are updated to {grade}")
    else:
        print("student not found")


def display_all_student():
    for name, grade in student_grades.items():
        print(f"{name}:{grade}")


def main():
    while True:
        print("\n Student Grades Management System ")
        print(" 1.Add Student ")
        print("2.Update")
        print("3. View all student")
        print("4. Exit \n")

        try:
            choice=int(input("Enter your choice"))
        except ValueError:
            print("Please enter a number")
            continue

        if choice==1:
            name=input("Enter student name=")
            try:
                grade=int(input("Enter student grades= "))
            except ValueError:
                print("Grade must be a number")
                continue
            add_student(name,grade)

        elif choice==2:
            name=input("Enter student name= ")
            try:
                grade=int(input("Enter student grades="))
            except ValueError:
                print("Grade must be a number")
                continue
            update_student(name,grade)

        elif choice==3:
            display_all_student()

        elif choice==4:
            print("closing the program")
            break
        else:
            print("Invalid choice")

if __name__=="__main__":
    main()
