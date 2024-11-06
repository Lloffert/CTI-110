# Lydia Loffert
# 11/6/2024
# P4HW2
#

# Get name from user or end program
userInput = input("""Enter employee's name or "Done" to terminate: """)

# Create variables to hold overtime calculations

#Loop to determine outcome of input
while userInput.lower() != "done":

    # Get employee information from user
    hours = float(input(f"How many hours did {userInput} work? "))
    
    # Determine whether employee worked overtime
    if hours > 40:
        OT = hours - 40
    else:
        OT = 0.0
    
    payRate = float(input(f"What is {userInput}'s pay rate? "))
    
    # Calculate overtime pay in a variable
    OT_pay = OT* payRate * 1.5
    
    print()
    print(f"Employee name: {userInput:>5}")
    print()
    print(f"{'Hours Worked':<16}{'Pay Rate':<16}{'OverTime':<16}{'OverTime Pay':<16}")
    print("-" * 60)
    print(f"{hours:<16.1f}{payRate:<16.2f}{OT:<16.1f}{OT_pay:<16.2f}")
    print()
    # Loop breaks    
    userInput = input("""Enter employee's name or "Done" to terminate: """)

    
print("Program finished- Bye!")
