#Lydia Loffert
#9/23/2024
#P1HW2
#Program that does some basic math on numbers that are entered.

#Psuedocode:
#Location & Budget
#3 charges: Fuel, Accomodations, and Food
#Budget - the 3 charges


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

print(f"Location: {destination} ")

print(f"Initial Budget: {budget} ")
print()

print(f"Fuel: {gas} ")
print(f"Accomodation: {hotel} ")
print(f"Food: {food} ")
print()

#Calculate remaining balance
leftover= budget -(gas + hotel + food)

#Display remaing balance
print(f"Remaining Balance: {leftover} ")
