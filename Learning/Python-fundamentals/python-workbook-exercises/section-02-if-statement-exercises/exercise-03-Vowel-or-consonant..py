'''Q3:-In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.'''

"""
Summary:- This program can check whether an alphabet is an vowel,consonant or a semi vowel. 
"""
# Displaying user what this program does
print("\nThis program can check whether an alphabet is an vowel or consonant or semi vowel\n")
# Taking user input 
L=input("\nEnter the alphabet that needs to be checked :- ")

# Calculating length of the input string to check whether user has entered more than one alphabet or not 
len=str.__len__(L)
if(L=='A' or L=='a' or L=='E' or L=='e' or L=='I' or L=='i' or L=='O' or L=='o' or L=='U' or L=='u'):
    
    print(f"\n{L} is a vowel\n")
elif(L=='Y' or L=='y' or L=='W' or L=='w'):

    print(f"\n{L} is a semi-vowel\n")

# ERROR HANDLING: What if user inputs more than one alphabet or a number or a special character
elif(len>1 or L==int(L) or L=='!' or L=='@' or L=='#' or L=='$' or L=='%' or L=='^' or L=='&' or L=='*' or L=='(' or L==')'):

    print("\nINVALID INPUT\n")

elif(L=='_' or L=='-' or L=='=' or L=='+' or L=='{' or L=='}' or L=='[' or L==']' or L==';' or L==':' or L=='|' or L=='<' or L=='>' or L==','):
    print("\nINVALID INPUT\n")

elif(L=='.' or L=='/' or L=='?' or L==' ' or L=='~'):
    print("\nINVALID INPUT\n")

else:
    
    print(f"\n{L} is a consonant\n")
