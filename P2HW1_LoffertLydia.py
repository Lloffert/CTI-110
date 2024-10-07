#Lydia Loffert
#10/7/2024
#P2HW1
#Recreate P1HW2 program with advanced formatting
#Desc of program
print("This program calculates and displays travel expenses")
print()

#User inputs travel info
budget= int(input("Enter Budget: "))
print()

destination= input("Enter your travel destination: ")
print()

gas= int(input("How much do you think you will spend on gas? "))
print()

hotel= int(input("Approximately, how much will you need for accomodation/hotel? "))
print()

food= int(input("Last, how much do you need for food? "))
print()

#Summarize travel expenses to user
print("------------Travel Expenses------------")

print(f"{'Location:':<25}{destination} ")
print(f"{'Initial Budget:':<25}${budget:.2f} ")
print(f"{'Fuel:':<25}${gas:.2f} ")
print(f"{'Accomodation:':<25}${hotel:.2f} ")
print(f"{'Food:':<25}${food:.2f} ")

print("-" * 39)

#Calculate remaining balance
leftover= budget -(gas + hotel + food)

#Display remaing balance
print(f"{'Remaining Balance:':<25}${leftover:.2f} ")
