"""
Irsan Sutanto
Lab 11, class in Python (extra points)
"""
class Student:
    def __init__(self, name, age):
        """
        Initializes the attributes of the Student class.
        Comments:
            name (str): The student's name.
            age (int): The student's age.
        """
        self.name = name
        self.age = age
        self.grades = {}  # Initialize an empty dictionary to store grades

    def add_grade(self, subject, grade):
        """
        Adds a grade for a particular subject.

        Args:
            subject (str): The name of the subject.
            grade (float): The grade for the subject.
        """
        self.grades[subject] = grade

    def get_average_grade(self):
        """
        Calculates and returns the average grade of the student.

        Returns:
            float: The average grade. Returns 0 if there are no grades.
        """
        if not self.grades:
            return 0.0  # Return 0 if the student has no grades
        total_grade = sum(self.grades.values())
        return total_grade / len(self.grades)

# CALLING THE CLASS
# Create instances and demonstrate usage of each method
# Create two Student objects
student1 = Student("Alice Smith", 20)
student2 = Student("Bob Johnson", 22)

# Add grades for student1
student1.add_grade("Math", 95.5)
student1.add_grade("Science", 89.0)
student1.add_grade("History", 92.3)

# Add grades for student2
student2.add_grade("Math", 88.0)
student2.add_grade("English", 91.2)

# Get and print the average grades for both students
average_grade_student1 = student1.get_average_grade()
average_grade_student2 = student2.get_average_grade()

print(f"{student1.name}'s grades: {student1.grades}")
print(f"{student1.name}'s average grade: {average_grade_student1:.2f}")  # Format to 2 decimal places
print(f"{student2.name}'s grades: {student2.grades}")
print(f"{student2.name}'s average grade: {average_grade_student2:.2f}")  # Format to 2 decimal places

#Demonstrate scenario with no grades
student3 = Student("Charlie Brown", 19)
print(f"{student3.name}'s grades: {student3.grades}")
average_grade_student3 = student3.get_average_grade()
print(f"{student3.name}'s average grade: {average_grade_student3:.2f}")
