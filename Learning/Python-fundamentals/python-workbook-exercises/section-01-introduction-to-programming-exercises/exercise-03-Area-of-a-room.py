'''Q3 :- Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with'''

# taking the length and breath from the user

l=float(input("please enter the length of a room in meters :- "))
b=float(input("please enter the width of a room in meters :- "))

area=l*b # calulated the area of a room since area of square or a rectangle is = length * breath

print(f"length of a room is ={l} \
       \nwidth of a room is {b} \
       \nthe area of the room is = {area} meters")

# printed the length, width and area of the room
#note :- i have used f string to print the values and \n to print the new line in the output
#also i have used \ to split the long print statement into two lines