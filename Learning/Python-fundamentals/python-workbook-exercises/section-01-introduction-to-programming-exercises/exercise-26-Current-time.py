'''Q26:-Python includes a library of functions for working with time, including a function
called asctime in the time module. It reads the current time from the computer’s internal clock and returns it in a human-readable format. Write a program
that displays the current time and date. Your program will not require any input from
the user.'''

"""
Summary:- this program wil give you current time one by default and another one you can format as u desire
"""

# Importing time module
import time

# Calling function asctime()-it will pick current time from the system unless time tuple is provided
current_time=time.asctime()

# Displaying current time using asctime() function 
print("\ncurrent time through asctime() function  is:- ",current_time)

# Formting time as year-month-date  hour:minute:seconds
format_time=time.strftime("%Y-%m-%d  %H:%M:%S")

# Displaying current time using strftime() function
print("formated time using strftime()function is = ",format_time)

# Experimenting with another format this time diplaying only a 24 hour clock
format_time=time.strftime("%H:%M:%S")

# Displaying results
print("24 hour clock format :- ",format_time)

# Expermenting with another format this time displaying 12 hour clock
format_time=time.strftime("%I:%M:%S")

# Displaying results
print("12 Hour clock format :- ",format_time)

# Greeting message
print("\nHAVE A NICE DAY\n")