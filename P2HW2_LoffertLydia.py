# Lydia Loffert
# 10/9/2024
# P2HW2
# Creat list program that stores grades entered in a list

#Create empty list
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

#Make variable for avergae of grades
avg = float(sum(grade_list) / 6)

# Display calculated results to user
print("-" * 12 + "Results" + "-" * 12)
print(f"{'Lowest Grade:':<19}{min(grade_list)}")
print(f"{'Highest Grade:':<19}{max(grade_list)}")
print(f"{'Sum of Grades:':<19}{sum(grade_list)}")
print(f"{'Average:':<19}{avg:.2f}")
print("-" * 40)




