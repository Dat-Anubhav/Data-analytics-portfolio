'''Q10:-It is common for images of a country's previous leaders, or other individuals of historical significance, 
to appear on its money. The individuals that appear on banknotes
in the United States are listed in Table 2.1.
Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the table:-

Individual          Amount

George Washington      $1
Thomas Jefferson       $2
Abraham Lincoln        $5
Alexander Hamilton     $10
Andrew Jackson         $20
Ulysses S. Grant       $50
Benjamin Franklin      $100'''
"""
Summary:- This program tells the individual that appears on the note if u enter the denomination of the note 
"""
# Displaying user objective of this program
print("\nThis program tells the individual that appears on the note if u enter the denomination of the note\n")
print("\nDenomination means different values of the currency notes such as $1, 2$,3$ etc\n")

# Taking user input
d=int(input("Please enter the denomination of the note which u want to check :- \n"))

if(d==1):
    print(f"\nThe individual on the ${d} note is :- George Washington\n")

elif(d==2):
    print(f"\nThe individual on the ${d} note is :- Thomas Jefferson\n")

elif(d==5):
    print(f"\nThe individual on the ${d} note is :- Abraham Lincoln\n")

elif(d==10):
    print(f"\nThe individual on the ${d} note is :- Alexander Hamilton\n")

elif(d==20):
    print(f"\nThe individual on the ${d} note is :- Andrew Jackson\n")

elif(d==50):
    print(f"\nThe individual on the ${d} note is :- Ulysses S. Grant\n")

elif(d==100):
    print(f"\nThe individual on the ${d} note is :- Benjamin Franklin\n")

else:
    print("\nINVALID INPUT\n")