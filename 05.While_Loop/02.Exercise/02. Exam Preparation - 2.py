number_bad_grades = int(input())
total_sum_of_grades = 0
number_of_problem = 0
last_problem = ""
count_of_bad_grades = 0
command = input()

while command != "Enough":
    last_problem = command
    current_grade = int(input())
    if current_grade <= 4:
        count_of_bad_grades += 1
        if count_of_bad_grades == number_bad_grades:
            print(f"You need a break, {count_of_bad_grades} poor grades.")
            break
    number_of_problem += 1
    total_sum_of_grades += current_grade
    command = input()
else:
    average_grade = total_sum_of_grades / number_of_problem
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {number_of_problem}")
    print(f"Last problem: {last_problem}")