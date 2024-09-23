#Lydia Loffert
#9/16/2024
#P1HW1
#Collect info from the user, processes info collected and display results

print("-----Calculating Exponents-----")
print()
print()

#Get integers from user
base_value= int(input("Enter an integer as the base value: "))

exponent= int(input("Enter an integer as the exponent: "))
print()
print()

#Display result to user
print(base_value, "rasied to the power of", exponent, "is", str(base_value**exponent) + "!!")

print("-----Addition and Subtraction-----")
print()
print()

#Get integers from user
start_num= int(input("Enter a starting integer: "))

add_num= int(input("Enter an intger to add: "))

sub_num= int(input("Enter an integer to subtract: "))
print()
print()

#Calculate the result
result= start_num + add_num - sub_num

#Display result
print(start_num, "+", add_num, "-", sub_num, "is equal to", result)
