'''Q14:-The horoscopes commonly reported in newspapers use the position of the sun at the
time of one’s birth to try and predict the future. This system of astrology divides the
year into twelve zodiac signs, as outline in the table below:

Zodiac sign         Date range

Capricorn       December 22 to January 19
Aquarius        January 20 to February 18
Pisces          February 19 to March 20
Aries           March 21 to April 19
Taurus          April 20 to May 20
Gemini          May 21 to June 20
Cancer          June 21 to July 22
Leo             July 23 to August 22
Virgo           August 23 to September 22
Libra           September 23 to October 22
Scorpio         October 23 to November 21
Sagittarius     November 22 to December 21

Write a program that asks the user to enter his or her month and day of birth. Then
your program should report the user's zodiac sign as part of an appropriate output
message.'''

# Displaying objective of this program to user
print("This program tells the Zodiac sign of a person based on his/her date of birth")
# Taking user input for month
M=input("\nPlease enter the month name of your date of birth =  ")

# Taking user input for the date
# it can crash my program if user entered anything other than an integer therefore using try-except block
try:

    d=int(input("\nPlease enter the day of your date of birth = "))

except ValueError:
    print("\nINVALID INPUT: Please enter in month and date format (ex: march 21,june 23, july 2 etc)\n")
    exit()

# Converting all the chharacters of the string to lower case 
# to reduce the number of conditions in the if statements
m=M.lower()
print(f"Your month and day of your date of birth is :-{M} {d} \n")


if(m=="december" and (d>=22 and d<=31)):
    
    print(f"\nZodiac sighn for your data of birth {m} {d} is = Capricon\n")

elif(m=="january" and (d>=1 and d<=19)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Capricon\n")

elif(m=="january" and (d>=20 and d<=31)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Aquarius\n")

elif(m=="february" and (d>=1 and d<=18)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Aquarius\n")

elif(m=="february" and (d>=19 and d<=29)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Pisces\n")

elif(m=="march" and (d>=1 and d<=20)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Pisces\n")

elif(m=="march" and (d>=21 and d<=30)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Aries\n")

elif(m=="april" and (d>=1 and d<=19)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Aries\n")

elif(m=="april" and (d>=20 and d<=31)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Taurus \n")

elif(m=="may" and (d>=1 and d<=20)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Taurus \n")

elif(m=="may" and (d>=21 and d<=30)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Gemini\n")

elif(m=="june" and (d>=1 and d<=20)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Gemini\n")

elif(m=="june" and (d>=21 and d<=31)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Cancer\n")


elif(m=="july" and (d>=1 and d<=22)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Cancer\n")

elif(m=="july" and (d>=23 and d<=30)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Leo\n")

elif(m=="august" and (d>=1 and d<=22)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Leo\n")

elif(m=="august" and (d>=23 and d<=31)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Virgo\n")

elif(m=="september" and (d>=1 and d<=22)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Virgo\n")

elif(m=="september" and (d>=23 and d<=30)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Libra\n")

elif(m=="october" and (d>=1 and d<=22)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Libra\n")

elif(m=="october" and (d>=23 and d<=31)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Scorpio\n")

elif(m=="november" and (d>=1 and d<=21)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Scorpio\n")

elif(m=="november" and (d>=22 and d<=30)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Sagittarius\n")

elif(m=="december" and (d>=1 and d<=21)):

    print(f"Zodiac sighn for your data of birth {m} {d} is = Sagittarius\n")

# ERROR HANDLING: if user enter short form of months like aug 21 mar 22 or aything else
else:
    print("\nINVALID INPUT\n")