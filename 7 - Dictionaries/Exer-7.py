def delete_students(dictionary):
    for student1, grades in dictionary.items():
        average_grade = sum(grades) / len(grades)
        if average_grade < 4.50:
            dictionary[student1] = None
        else:
            dictionary[student1] = average_grade
    dictionary = {student1: grades for student1, grades in dictionary.items() if grades is not None}
    return dictionary


num_of_rows = int(input())
students = {}

for _ in range(num_of_rows):
    name = input()
    grade = float(input())
    if name not in students.keys():
        students[name] = []
    students[name].append(grade)

students = delete_students(students)
students = {k: v for k, v in sorted(students.items(), key=lambda item: item[1], reverse=True)}

for student, grade in students.items():
    print(f'{student} -> {grade:.2f}')
