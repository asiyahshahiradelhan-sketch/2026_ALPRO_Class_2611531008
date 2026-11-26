students = input().split()
submitted = input().split()

submitted_set = set(submitted)

not_submitted = set(students) - submitted_set

print("Submitted:", len(set(students) & submitted_set), "students")
print("Not submitted:", len(not_submitted), "students")

for student in students:
    if student in not_submitted:
        print(student)