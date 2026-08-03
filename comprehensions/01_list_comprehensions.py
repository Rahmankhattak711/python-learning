student_name = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Henry",
    "Ivy",
    "Jack",
]

find_student_name = [
    student_name for student_name in student_name if len(student_name) >= 4
]

print(find_student_name)
