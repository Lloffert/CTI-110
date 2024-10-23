# Lydia Loffert
# 10/14/2024
# P3LAB
# Calculate the most efficient number of change needed
'''
#Regular division
print(100/3)

#Floor division - returns ONLY integer portion of quotient
print(100//3)

#Modulo - returns ONLY the remainder
print(100%3)
print(7%4)
'''
# Get amount of money from user as a float
money = float(input("Enter the amount of money as a float: $"))

# Convert money to a whole number
money = round(money * 100)

#Scenario for when there is no money entered
if money == 0:
    print("No change")

# May need to round this value
# money = int(money * 100)

# Get whole dollars from money amount
dollars = money // 100

# Remove dollar amount from money value
money = money - (dollars * 100)

# Get quarters from money amount
quarters = money // 25

# Remove quarter amount from money value
money = money - (quarters * 25)

# Get dimes from money amount
dimes = money // 10

# Remove dime amount from money value
money = money - (dimes * 10)

# Get nickels from money amount
nickels = money // 5

# Remove nickel amount from money value
money = money - (nickels * 5)

# Get pennies from money amount
pennies = money

# Display number of dollars and coins needed

if dollars >= 1:
    if dollars == 1:
        print(f"{dollars} dollar")
    else : # more than one dollar
        print(f"{dollars} dollars")
            
if quarters >= 1:
    if quarters == 1:
        print(f"{quarters} quarter")
    else : # more than one quarter
        print(f"{quarters} quarters")        
      
if dimes >= 1:        
    if dimes == 1:
        print(f"{dimes} dime")
    else : # more than one dime
        print(f"{dimes} dimes")
        
if nickels >= 1:
    if nickels == 1:
        print(f"{nickels} nickel")
    else : # more than one nickel
        print(f"{nickels} nickels")
        
if pennies >= 1:
    if pennies == 1:
        print(f"{pennies} penny")
    else : # more than one penny
        print(f"{pennies} pennies")


