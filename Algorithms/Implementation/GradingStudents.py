#!/bin/python3
def solve(grades):
    # Complete this function
    return [x + 5 - x % 5 if x % 5 >= 3 and x >= 38 else x for x in grades]


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))

# Editors solution
n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())

    if grade >= 38:
        # Here, we are only ever calculating 'grade mod 5' once:
        mod5 = grade % 5

        if mod5 >= 3:
            grade = grade + (5 - mod5)

    print(grade)
