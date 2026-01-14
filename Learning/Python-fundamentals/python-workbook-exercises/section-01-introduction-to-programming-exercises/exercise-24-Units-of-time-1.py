'''Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.'''

# Displaying the motive of this program
print("\nThis program will tell your total duration in seconds")

# Taking user input for his/her total duration
print("\nEnter your duration in number of days,hours,minutes and seconds :- ")

t1=int(input("\n Enter the number of days :- "))
t2=int(input("\n Enter the number of hours :- "))
t3=int(input("\n Enter the number of minutes :- "))
t4=int(input("\n Enter the number of seconds :- "))

# Telling the user that your inputs are within the range or not

if(t1<0):# for negative input of days
    t1=0
    print("\nINVALID DAYS INPUT\n")
elif(t1>=365):
    print("\nyou are exceeding the range of days in a year \n\
But we can still calculate your total duration in seconds")

if(t2<0):# for negative input of hours
    t2=0
    print("\nINVALID HOURS INPUT\n")

elif(t2>=24):
    print("\nyou are exceeding the range of hours in day \n\
But we can still calculate your total duration in seconds")

if(t3<0):# for negative input of minutes
    t3=0
    print("\nINVALID MINUTES INPUT\n")

elif(t3>=60):
    print("\nyou are exceeding the range of minutes in a hour \n\
But we can still calculate your total duration in seconds")

if(t4<0):# for negative input of seconds
    t4=0
    print("\nINVALID SECONDS INPUT\n")

elif(t4>=60):
    print("\nyou are exceeding the range of minutes \n\
But we can still calculate your total duration in seconds")

#If all the inputs are negative or zero then Displaying an appropriate message to the user. 
elif(t1==0 and t2==0 and t3==0 and t4==0):
    print("\nALL INPUTS ARE WRONG OR ZERO\n")    
else:
    print("\nYour some inputs are within the range of days in a year , hours in a day , minutes in a hour , and seconds in a minute  ")
#Calculating the total duration of the user by converting days to hours hoursto minutes and minutes to seconds 

s=t1*24*60*60 # 1 day = 24 hours,1 hour=60 minutes, 1 minute= 60 seconds.
s=s+(t2*60*60) # 1 hour=60 minutes, 1 minute= 60 seconds.
s=s+(t3*60)   # 1 minute= 60 seconds.
s=s+t4 # t4 is already in seconds no need to convert it.

# Displaying the users total number of duration in seconds
print(f"\nYour total duration in seconds are :- {s} seconds\n")

# displaying greetings
print("\nHAVE a NICE DAY :)\n")