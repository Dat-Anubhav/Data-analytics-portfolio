'''The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
The value 6371.01 in the previous equation wasn’t selected at random. It is
the average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers'''


print("enter the cordinates :- \n")

# taking the user input for latitude and longitude of two points on earth
t1=float(input("enter the latitude of the point 1 (t1) :- "))

g1=float(input("enter the longitude of point 1 (g1):- "))

t2=float(input("enter the latitude of the point 2 (t2) :- "))

g2=float(input("enter the longitude of point 2 (g2) :- "))

import math

# converting the user input which is in number or float value into radians for better calculations
t1=math.radians(t1)
t2=math.radians(t2)
g1=math.radians(g1)
g2=math.radians(g2)

# calculating the distance between the two points on earth using the formula given above
distance= 6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))

# displaying the result
print(f"the distance between the two points on earth i.e point 1 :- {t1,g1} and point 2 {t2,g2} is = {distance} km")

