#PhillipsP1
#Programmer: Garrett Phillips
#EMail: gphillips12@cnm.edu
#Purpose: Provides user ability to calculate volume of a pyramid
#Python Version: 2.5


#Length of the base: a Height of the pyramid: h
# Volume = a^2h / 3 Slant height,
# s = sqrt(h2 + (a / 2) 2) This is the Pythagorean Theorem part.
# Area of one pyramid side = s * a / 2

#brings in the math functions
import math
from math import sqrt

print ("Hi, I'm the pyramid calculator. I am here to calculate your pyramid!")
print ("The pyramid must be a square pyramid!")

#asks the user information about the pyramid
h = input ("What is the height of your pyramid (in feet)?")
a = input ("What is the length of the base of your pyramid (in feet)?")

#finds the overall volume of the pyramid
v = ((a**2)*h)/3

#finds the slant height
s = sqrt(h**2+(a/2)**2)
#finds the area of one side of the pyramid
AoS = (s*a)/2
#finds the total surface area of the pyramid
totS = AoS*5

#displays the height, base, total surface area, volume rounded to the third decimal place
print "The height of your pyramid is " , h, " feet."
print "The area of one side of the pyramid is roughly " , str(round(AoS , 3)) , "square feet."
print "The total surface area of the pyramid is roughly " , str(round(totS, 3)), "sqare feet."
print "The volume of your pyramid is roughly ", str(round (v, 3)), "cubic ft."

exit()
