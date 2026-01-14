'''Q15:-The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
shown in the table below. The pattern repeats from there, with 2012 being another
year of the dragon, and 1999 being another year of the hare.

Year    Animal

2000    Dragon
2001    Snake
2002    Horse
2003    Sheep
2004    Monkey
2005    Rooster
2006    Dog
2007    Pig
2008    Rat
2009    Ox
2010    Tiger
2011    Hare

Write a program that reads a year from the user and displays the animal associated
with that year. Your program should work correctly for any year greater than or equal
to zero, not just the ones listed in the table.'''

# Displaying the objective of the program
print("\nThis program tells the chinese Zodiac sighns assigns to animals \n")

# ERROR HANDLING: what if user input random keys on keyboard or enter year in spelling or string format like 
# twenty twenty five for 2025
try:
    # Taking user input
    y=int(input("\nPlease enter the year you want to check :-"))
except ValueError:
   print("\nINVALID INPUT: Please enter in integer format (ex: 2011, 1999, 2023, 2025 etc)\n")
   exit()

# ERROR HANDLING: years can't be in negative
if(y<0):
   print("\nINVALID INPUT: Negative numbering is usually not found in historical texts, \
\nand it doesn't apply here either.\n")

elif((y-2000)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = DROGON\n")

elif((y-2001)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = SNAKE\n")

elif((y-2002)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = HORSE\n")

elif((y-2003)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = SHEEP\n")

elif((y-2004)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = MONKEY\n")

elif((y-2005)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = ROOSTER\n")

elif((y-2006)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = DOG\n")

elif((y-2007)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = PIG\n")

elif((y-2008)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = RAT\n")

elif((y-2009)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = OX\n")

elif((y-2010)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = TIGER\n")

elif((y-2011)%12==0):
   print(f"\nThe Chinese Zodiac sighn assign to {y} is = HARE\n")


