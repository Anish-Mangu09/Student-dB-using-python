class Student:
    def __init__(self, student_id, name, marks):
        self.__student_id = student_id
        self.__name = name
        self.__marks = marks

    def display(self):
        print(f"ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Marks: {self.__marks}")
        print("-" * 20)

    def get_id(self):
        return self.__student_id

    def update_marks(self, new_marks):
        self.__marks = new_marks


class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = Student(student_id, name, marks)
        self.students.append(student)

        print("Student Added Successfully!\n")

    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        sid = int(input("Enter Student ID to Search: "))

        for student in self.students:
            if student.get_id() == sid:
                print("Student Found:")
                student.display()
                return

        print("Student Not Found.")

    def update_student_marks(self):
        sid = int(input("Enter Student ID: "))

        for student in self.students:
            if student.get_id() == sid:
                new_marks = float(input("Enter New Marks: "))
                student.update_marks(new_marks)
                print("Marks Updated Successfully!")
                return

        print("Student Not Found.")

    def delete_student(self):
        sid = int(input("Enter Student ID to Delete: "))

        for student in self.students:
            if student.get_id() == sid:
                self.students.remove(student)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found.")


# Main Program
db = StudentDatabase()

while True:
    print("\n===== STUDENT DATABASE SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        db.add_student()
    elif choice == "2":
        db.display_students()
    elif choice == "3":
        db.search_student()
    elif choice == "4":
        db.update_student_marks()
    elif choice == "5":
        db.delete_student()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid Choice!")