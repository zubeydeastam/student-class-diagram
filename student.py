class Student:
    def __init__(self, student_id, name, department, gpa):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.gpa = gpa
        self.is_enrolled = True

    def honor_status(self):
        if self.gpa >= 3.0:
            print(self.name, "is on the honor list.")
        else:
            print(self.name, "is not on the honor list.")

    def update_gpa(self, new_gpa):
        if 0.0 <= new_gpa <= 4.0:
            self.gpa = new_gpa
            print(self.name, "GPA updated to", self.gpa)
        else:
            print("Invalid GPA value.")

    def show_info(self):
        print("ID:", self.student_id, "| Name:", self.name, "| Dept:", self.department, "| GPA:", self.gpa, "| Enrolled:", self.is_enrolled)


# Test
student1 = Student("20243086", "Zubeyde Astam", "Computer Engineering", 3.5)
student1.show_info()

student1.honor_status()
student1.update_gpa(3.8)
student1.show_info()
