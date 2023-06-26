#
# num_students = int(input("Enter the number of students: "))
# num_subjects = int(input("Enter the number of subjects: "))
#
#
# grades = []
#
#
# for i in range(num_students):
#     for j in range(num_subjects):
#         grade = float(input("Enter the grade for student {} in subject {}: ".format(i + 1, j + 1)))
#         grades.append(grade)
#
#
# total_students = len(grades)
#
# average_grade = sum(grades) / total_students
#
# print("The total number of students is:", total_students)
# print("The average grade is:", average_grade)


def calculate_average_grade():
    num_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects: "))

    total_grade = 0
    student_count = 1

    while student_count <= num_students:
        print(f"\nStudent {student_count}:")
        total_student_grade = 0
        subject_count = 1

        while subject_count <= num_subjects:
            grade = float(input(f"Enter grade for Subject {subject_count}: "))
            total_student_grade += grade
            subject_count += 1

        total_grade += total_student_grade
        student_average = total_student_grade / num_subjects
        print(f"Average grade for Student {student_count}: {student_average:.2f}")

        student_count += 1

    class_average = total_grade / (num_students * num_subjects)
    print(f"\nTotal number of students: {num_students}")
    print(f"Average grade for the class: {class_average:.2f}")


calculate_average_grade()
