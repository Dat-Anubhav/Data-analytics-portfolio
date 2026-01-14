'''Q25:- Write a program that reads a date from the user and computes its immediate successor.
For example, if the user enters values that represent 2013-11-18 then your program
should display a message indicating that the day immediately after 2013-11-18 is
2013-11-19. If the user enters values that represent 2013-11-30 then the program
should indicate that the next day is 2013-12-01. If the user enters values that represent
2013-12-31 then the program should indicate that the next day is 2014-01-01. The
date will be entered in numeric form with three separate input statements; one for
the year, one for the month, and one for the day. Ensure that your program works
correctly for leap years.'''

# Displaying the objective of this program to user
print("\nThis program determines the following day based on the date that you enter.\n")

# Prompting the user to enter the date in year-month-day format
print("\nPlease enter the date in year-month-day format\n")

# Preventing program from crashing: what if user input in string or in float
try:
    # Taking user input for year  
    y=int(input("\nPlease enter the year :- "))
    
    #Taking user input for month 
    m=int(input("\nPlease enter the month :- "))
    
    # Taking user input for day
    d=int(input("\nPlease enter the day :- "))

except ValueError:
      print("\nINVALID INPUT: Please enter the correct format (ex:2025-10-16)\n")
      exit()


# Checking conditions for January month
if(m==1):

    if(d<31):

            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==31):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")
# Checking conditions for February month
elif(m==2):
    
    if(y%400==0):
        print(f"\nEntered date {y}-{m}-{d} is a leap year\n")
        
        if(d<=28):
              D=d+1
              print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
        elif(d==29):
            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
        else:
            print("\nINVALID DAY INPUT\n")    
    
    elif(y%100==0):
        print(f"\nEntered date {y}-{m}-{d} is not a leap year\n")
           
        if(d==29):
            print(f"\nEntered date {y}-{m}-{d}: Invalid day input\n")      
            exit()



        if(d<28):
        
            D=d+1
            
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
        elif(d==28):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
        
        else:
            print("\nINVALID DAY INPUT\n")        
    
    elif(y%4==0):
        print(f"\n\nEntered date {y}-{m}-{d} is a leap year")
        
        if(d<=28):
              D=d+1
              print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
        elif(d==29):
            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
        else:
            print("\nINVALID DAY INPUT\n")

    else:
        print("\nEntered date {y}-{m}-{d} is not a leap year\n")
           
        if(d==29):
            print(f"\nentered date is {y}-{m}-{d}: Invalid day input\n")      
            exit()



        if(d<28):
        
            D=d+1
            
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
        elif(d==28):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
        else:
            print("\nINVALID DAY INPUT\n")          

# Checking conditions for March month        
elif(m==3):

    if(d<31):

            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==31):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")

# Checking conditions for April month    
elif(m==4):

    if(d<30):
            
            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==30):
            
            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")

# Checking conditions for May month    
elif(m==5):

    if(d<31):

            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==31):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")

# Checking conditions for June month        
elif(m==6):

    if(d<30):

            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==30):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")

# Checking conditions for July month        
elif(m==7):

    if(d<31):

            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==31):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")

# Checking conditions for August month    
elif(m==8):

    if(d<31):

            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==31):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")

# Checking conditions for September month
elif(m==9):

    if(d<30):

            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==30):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")

# Checking conditions for October month
elif(m==10):

    if(d<31):

            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==31):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")

# Checking conditions for November month
elif(m==11):

    if(d<30):

            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==30):

            M=m+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{M}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")

# Checking conditions for December month
elif(m==12):

    if(d<31):

            D=d+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {y}-{m}-{D}\n")
        
    elif(d==31):

            Y=y+1
            print(f"\nEntered date {y}-{m}-{d}, Next day = {Y}-{1}-{1}\n")
    else:
          print("\nINVALID DAY INPUT\n")

# ERROR HANDLING: If the user inputs a month value that is outside the range of 1 to 12.
else:
      print("\nINVALID INPUT\n")