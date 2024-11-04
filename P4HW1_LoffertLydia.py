# Lydia Loffert
# 11/4/2024
# P4HW1
#

# Get the number of scores from the user
sc_amount = int(input("How many scores do you want to enter? "))

# Empty list to hold valid scores
validScores = []

print()

# For loop to allow user to enter scores
for scores in range(0,sc_amount):
    userInput = float(input(f"Enter score #{scores + 1}: "))

# User is asked to re-enter score if negative
    while userInput < 0 or userInput > 100:
        print()
        print("INVALID Score entered!!!!\nScore should be between 0 and 100")
        userInput = float(input(f"Enter score #{scores + 1}: "))

    # Add valid scores to empty list
    validScores.append(userInput)
#For loop breaks

print()

# Calculate average of scores
avg = float(sum(validScores) / sc_amount)

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
    
#Print results
print("-" * 12 + "Results" + "-" * 12)
print(f"Lowest Score  : {min(validScores)}")
    
# Remove lowest score from list
validScores.remove(min(validScores))

print(f"Modified List : {validScores}")
print(f"Scores Average: {avg:.2f}")
print(f"Grade{':':>10} {letter_grade}")
    
#Loop breaks
print("-" * 31)
