'''Q-4 :- Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.'''

#taking the length and breath of farmers field from the user

l=float(input("Please enter the farmers length of the field in feet :- "))
b=float(input("Please enter the breath of the farmers field in feet :- "))

area= l*b  #area in feet
area=area/43560# area in acres since 1 acre = 43560 feet

print(f"the length of the farmers field in feet ={l}\
      \nthe breath of the farmers fielf in feet = {b}\
      \nthe Area of the farmers field in acres = {area}")

# here i make use of f string to print the values and \n to print the new line in the output
#  i used \ to split the long print statement

