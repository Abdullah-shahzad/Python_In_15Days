# Define the Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, subject, grade):
        self.grades.append((subject, grade))

    def average_grade(self):
        if not self.grades:  # Check if the student has no grades
            return 0
        total = sum(grade for subject, grade in self.grades)
        return total / len(self.grades)

    def __str__(self):
        avg_grade = self.average_grade()
        grades_str = ', '.join([f"({subject}, {grade})" for subject, grade in self.grades])
        return f"{self.name}, ID: {self.student_id}, Average Grade: {avg_grade:.2f}, Grades: [{grades_str}]"


# Function to add students and grades from input data
def add_students_and_grades(data):
    students = {}

    for name, student_id, subject, grade in data:
        if student_id not in students:
            students[student_id] = Student(name, student_id)
        students[student_id].add_grade(subject, grade)

    return list(students.values())


# Function to filter students by average grade
def filter_students_by_grade(students, threshold):
    return [student for student in students if student.average_grade() > threshold]


# Function to display students' details
def display_students(students):
    for student in students:
        print(student)


# Main program execution
if __name__ == "__main__":
    # Example input data
    students_data = [
        ("Alice", "001", "Math", 85),
        ("Alice", "001", "Science", 90),
        ("Bob", "002", "Math", 78),
        ("Charlie", "003", "Math", 92),
        ("Charlie", "003", "History", 88),
    ]

    # Add students and their grades
    students = add_students_and_grades(students_data)

    # Display all students
    print("All Students:")
    display_students(students)

    # Filter and display students with an average grade above 85
    print("\nStudents with an average grade above 85:")
    filtered_students = filter_students_by_grade(students, 85)
    display_students(filtered_students)
