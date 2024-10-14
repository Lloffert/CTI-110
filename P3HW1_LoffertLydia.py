# Lydia Loffert
# 10/14/2024
# P3HW1
# Use branching to determine a letter grade

# Create empty list
grade_list = []

# User inputs module grades
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
print()

# Add variables to the list
grade_list.append(mod1)
grade_list.append(mod2)
grade_list.append(mod3)
grade_list.append(mod4)
grade_list.append(mod5)
grade_list.append(mod6)

# Make variable for average of grades
avg = float(sum(grade_list) / 6)

# Display calculated results to user
print("-" * 12 + "Results" + "-" * 12)
print(f"{'Lowest Grade:':<19}{min(grade_list)}")
print(f"{'Highest Grade:':<19}{max(grade_list)}")
print(f"{'Sum of Grades:':<19}{sum(grade_list)}")
print(f"{'Average:':<19}{avg:.2f}")
print("-" * 40)

# Create the branching to  get letter grade
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print(f"Your grade is: {letter_grade}")
