# University System to display information

# Superclass
class Person:
    def __init__(self, name, registration_number):
        self.name = name
        self.registration_number = registration_number

    def display_info(self):
        print(f'Name: {self.name}, ID: {self.registration_number}')


# Subclass: Student
class Student(Person):
    def __init__(self, name, registration_number, course, year):
        super().__init__(name, registration_number)
        self.course = course
        self.year = year


    def display_info(self):
        super().display_info()
        print(f'Course: {self.course}, Year: {self.year}')


# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, id_number, department, salary):
        super().__init__(name, id_number)
        self.department = department
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f'Department: {self.department}, Salary: {self.salary}')


# Subclass: Staff
class Staff(Person):
    def __init__(self, name, id_number, position, salary):
        super().__init__(name, id_number)
        self.position = position
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f'Position: {self.position}, Salary: {self.salary}')


student = Student('Alice Johnson', 'S123456', 'Computer Science', 'Sophomore')
lecturer = Lecturer('Dr. Bob Smith', 'L987654', 'Mathematics', 75000)
staff = Staff('Eve Davis', 'ST112233', 'Administrative Assistant', 40000)

print("Student Information:")
student.display_info()
print("\nLecturer Information:")
lecturer.display_info()
print("\nStaff Information:")
staff.display_info()