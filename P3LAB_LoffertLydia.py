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

# May need to round this value
# money = int(money * 100)

# Get whole dollars from money amount
dollars = money // 100
print(f"{dollars} Dollars")
# Remove dollar amount from money value
money = money - (dollars * 100)

# Get quarters from money amount
quarters = money // 25

# Remove quarter amount from money value
money = money - (quarters * 25)
print(f"{quarters} Quarters")

# Get dimes from money amount
dimes = money // 10

# Remove dime amount from money value
money = money - (dimes * 10)
print(f"{dimes} Dimes")

# Get nickels from money amount
nickels = money // 5

# Remove nickel amount from money value
money = money - (nickels * 5)
print(f"{nickels} Nickels")

# Get pennies from money amount
pennies = money
print(f"{pennies} Pennies")
