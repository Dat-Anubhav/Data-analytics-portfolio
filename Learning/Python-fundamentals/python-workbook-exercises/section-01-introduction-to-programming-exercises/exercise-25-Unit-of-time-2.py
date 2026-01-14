'''In this exercise you will reverse the process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary.'''

print("\nThis program helps you to convert secconds into a order of days:hours:minutes:seconds\n")

# Taking user input
s=int(input("\nEnter the total duration in seconds :- "))

# "All calculations are performed using seconds as the base unit; 
# converting stepwise to days, hours, and minutes can be complex and error-prone."

# 1 day has 86400 seconds : 1*24*60*60=86400
D=s//86400
r=s%86400 # remaning seconds for further calculations

# 1 hour has 3600 seconds : 1*60*60=3600
H=r//3600
r=r%3600

# 1 minute has 60 seconds
M=r//60
r=r%60

S=r

# Displaying results in DAYS:HOURS:MINUTES:SECONDS format
print(f"\nTotal seconds = {s}\n\
DD:HH:MM:SS :- {D}:{H}:{M}:{S}\n")

