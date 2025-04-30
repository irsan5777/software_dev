"""
Irsan Sutanto
Lab 11, class in Python (extra points)
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = {}   # Initialize an empty dictionary to store grades

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0.0  
        total_grade = sum(self.grades.values())
        return total_grade / len(self.grades)

student1 = Student("Susan Wayne", 20)
student1.add_grade("Math", 95.5)
student1.add_grade("Science", 89.0)
student1.add_grade("History", 92.3)

student2 = Student("Joey Doey", 22)
student2.add_grade("Math", 88.0)
student2.add_grade("English", 91.2)

student3 = Student("Pablo Hemming", 24)
student3.add_grade("Math", 55.5)
student3.add_grade("History", 55.5)
student3.add_grade("Science", 50.0)

print(f"Name : {student1.name},  your age is : {student1.age}, your grades are : {student1.grades}, your average grade is : {student1.get_average_grade():.2f}")
print(f"Name : {student2.name},    your age is : {student2.age}, your grades are : {student2.grades},           your average grade is : {student2.get_average_grade():.2f}")
print(f"Name : {student3.name}, your age is : {student3.age}, your grades are : {student3.grades}, your average grade is : {student3.get_average_grade():.2f}")

