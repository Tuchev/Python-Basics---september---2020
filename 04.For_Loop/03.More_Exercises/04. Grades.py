number_of_students = int(input())
top_students = 0
very_good_students = 0
good_students = 0
fail_students = 0
average_success = 0

for grade in range(number_of_students):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        fail_students += 1
        average_success += grade
    if 3.00 <= grade <= 3.99:
        good_students += 1
        average_success += grade
    if 4.00 <= grade <= 4.99:
        very_good_students += 1
        average_success += grade
    if grade >= 5:
        top_students += 1
        average_success += grade
print(f"Top students: {((top_students / number_of_students) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((very_good_students / number_of_students) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((good_students / number_of_students) * 100):.2f}%")
print(f"Fail: {((fail_students / number_of_students) * 100):.2f}%")
print(f"Average: {(average_success / number_of_students):.2f}")