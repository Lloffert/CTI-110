# Learning to use user-defined function

# Define a multiply function
def multiply(num1, num2, num3):
    product = num1 * num2 * num3
    print(product)

# Define an add function
def add(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)

def returnNum():
    userInput = input("Give me a big number: ")
    while not userInput.isnumeric():
        print("Value must be a number")
        userInput = input("Give me a big number: ")
    return int(userInput)

def getName(lastName):
    name = input("Enter your first name: ")
    fullname = "User " + name + lastName
    return fullname

# Define the main function - all your logic goes here
def main():
    # Get input from user
    first_num = int(input("Give me a number: "))
    sec_num = int(input("Give me a number: "))
    third_num = int(input("Give me a number: "))

    # Call the multiply function
    multiply(first_num, sec_num, third_num)

    # Call the add function
    add(first_num, sec_num, third_num)

    # Call the value returning function
    bigNum = returnNum()

    print(bigNum * 5)
    print(getName(" Loffert"))


# Call the main function
if __name__ == "__main__":
    main()