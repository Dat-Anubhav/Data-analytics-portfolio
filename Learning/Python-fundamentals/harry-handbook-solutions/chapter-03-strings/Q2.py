"""Q2 :- Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
''' """

"""
Summary:-This program demonstrates how to use string replacement to fill a template with variables.
"""

# Option 1:taking user input
# name = input("enter your name :- ")
# date = input("enter the date :- ")
# print(f"Dear {name} \n you are selected! \n {date} CONGRATULATIONS")


#       OR          

# Option 2: direct assignment
name = "Anubhav"
date = "14 September"
letter = "Dear <name>,\nYou are selected!\n<date>\nCONGRATULATIONS" 
m= letter.replace("<name>",name).replace("<date>",date)

# printing the modified letter
print(m)