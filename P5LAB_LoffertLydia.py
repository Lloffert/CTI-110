# Lydia Loffert
# 11/13/2024
# P5LAB
# Simulate self-checkout using functions

# Import the random library
import random

def disperse_change(money):
    
        # Convert money to a whole number
    money = int(round(money * 100, 2))

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


# Define the main function
def main():
    print("Welcome to the store")
    print()
    
    # Generate money owed
    cost = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${cost:.2f}")

    # Ask customer how much they're paying
    payment = float(input("How much cash will you put in the self-checkout? $"))
    money = payment - cost
    money = round(money, 2)
    print(f"Change is: ${money}")
    print()

    # Call disperse_change function to display coin amount
    disperse_change(money)
    
# Call the main
if __name__ == "__main__":
    main()
