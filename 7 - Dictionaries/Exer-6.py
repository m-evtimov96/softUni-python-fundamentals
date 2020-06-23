courses = {}

while True:
    input_line = input()
    if input_line == 'end':
        break
    course, student = input_line.split(' : ')
    if course not in courses.keys():
        courses[course] = []
    courses[course].append(student)

sorted_courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))
for course, students in sorted_courses.items():
    print(f'{course}: {len(students)}')
    students.sort()
    for student in students:
        print(f'-- {student}')
