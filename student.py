class Student:
    def __init__(self, student_id: str, name: str, department: str, gpa: float):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.gpa = gpa

    def is_honor_student(self) -> bool:
        return self.gpa >= 3.0

    def display_info(self) -> None:
        print(f"ID: {self.student_id} | Name: {self.name} | Dept: {self.department} | GPA: {self.gpa}")


if __name__ == "__main__":
    student = Student("20243086", "Zubeyde Astam", "Computer Engineering", 3.5)
    student.display_info()
    print("Honor Student:", student.is_honor_student())
