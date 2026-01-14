'''Q3 :- Write a program to detect double space in a string.'''

# This program demonstrates how to detect and replace double spaces in a string.

# Taking input from the user
str = input("enter the string :- ")

m = str.find("  ")

print(m==-1,"Statement : There is no double space in the string")
print(m!=1,"Statement : There is double or extra space in the string")

# can be done more correctly with if else staements but this chapter comes before the if else chapter 
# therefore i am not using it here

'''The strip() function only removes spaces from the beginning and end of the string.
It does NOT remove double or extra spaces between words inside the string.'''
# therefore it is better to use find() method to check double space in the string

    
     # you can just use str.find("  ") if it gives minus -1 then no double space
    #  if any other index nubmber means it has double space at that index number 


'''Q4:- Replace the double space from problem 3 with single spaces.'''

#Replacing double space with single space 
m=str.replace("  "," ")

# printing the modified string
print("replacing the double space with the single space :-",m)