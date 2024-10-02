#In-class examples using dictionary

#Create a dictionmary using key :value pairs

person1= {"name":input("Enter name: "), "age":54, "height":5.8,}

#Get info from dictionary using the key
print(person1["name"])

#print the entire diictionaries
print(person1)
print("\n\n")

#add key value pair to dictionary
person1["DOB"]= "10-20-1990"
print(person1)
print("\n\n")

person1.update({"hair_color":"brown"})
print(person1)
print("\n\n")

#delete key value from dictionary
del person1["height"]
print(person1)
print("\n\n")

#Create key:value pair from user input
person1["height"]= input(f"Enter height of {person1['name']}: ")
print(person1)
print("\n\n\n\n")

#User picks the information to get out of dictionary

print(person1.keys(), "\n")
userChoice= input(f"What would you like to know about {person1['name']}? ")
print()
print(person1[userChoice])
