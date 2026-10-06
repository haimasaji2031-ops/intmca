# Student Grade Calculator

def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


print("Student Grade Calculator")

student_name = input("Enter student name: ")
mark = float(input("Enter student mark (0-100): "))

if 0 <= mark <= 100:
    grade = calculate_grade(mark)

    print("\nStudent:", student_name)
    print("Mark:", mark)
    print("Grade:", grade)
else:
    print("Please enter a mark between 0 and 100.")
