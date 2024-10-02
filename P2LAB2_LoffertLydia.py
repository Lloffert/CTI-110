#Lydia Loffert
#10/2/2024
#P2LAB2
#Create a dictionary that stores user input and displays output to the user

#Create dictionary from given key:value pairs

cars_mpg = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

#Print all dictionary keys
print(cars_mpg.keys())
print()

#Get car (key) from user
userCar = input("Enter a vehicle to see it's mpg: ")
print()

#Display mpg for the userCar
print(f"The {userCar} gets {cars_mpg[userCar]} mpg.")
print()

#Get planned mileage from user
userMiles = int(input(f"How many miles will you drive the {userCar}? "))
print()

#Calculate gallons of gas needed
total_gas = userMiles/cars_mpg[userCar]

#Display total gas needed to user
print(f"{total_gas:.2f} gallon(s) of gas are needed to drive the {userCar} {userMiles} miles.")
