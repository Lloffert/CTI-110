#Lydia Loffert
#9/30/2024
#P2LAB1
#Using imported library, math, and f-string.

#Import math library
import math

#Get the radius from the user
radius= float(input(f"What is the  radius of the circle? "))
print()

#Calculate diameter
diameter=2*radius

#Display diameter with one decimal place
print(f"The diameter of the circle is {diameter:.1f}")
print()

#Calculate circumference
circum=2*math.pi*radius

#Display circumference with two decimal places
print(f"The cicrumference of the circle is {circum:.2f}")
print()

#Calculate area
area=math.pi*radius**2

#Display area with three decimal places
print(f"The area of the circle is {area:.3f}")
