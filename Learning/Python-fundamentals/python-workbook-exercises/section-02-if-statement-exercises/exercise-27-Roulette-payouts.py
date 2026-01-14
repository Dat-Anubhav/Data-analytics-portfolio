'''Q27:-A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
between 1 and 36 are used to number the black spaces.
Many different bets can be placed in roulette. We will only consider the following
subset of them in this exercise:

• Single number (1 to 36, 0, or 00)
• Red versus Black
• Odd versus Even (Note that 0 and 00 do not pay out for even)
• 1 to 18 versus 19 to 36

Write a program that simulates a spin of a roulette wheel by using Python’s random
number generator. Display the number that was selected and all of the bets that must
be payed. For example, if 13 is selected then your program should display:

The spin resulted in 13...
Pay 13
Pay Black
Pay Odd
Pay 1 to 18

If the simulation results in 0 or 00 then your program should display Pay 0 or
Pay 00 without any further output'''

# Displaying the objective of this program to user
print("\nWelcome to the Roulette Payout Game! \
This program spins a virtual roulette wheel and shows the payouts.\n")


# Displaying the opening message before the spin
print("\nWelcome! Let's spin the roulette wheel.\n")

# Importing the random module to generate a random number
import random
a=random.randint(1,38)

# Map 37 to '0' and 38 to '00' to represent green slots on the roulette wheel
if(a==37):
    
    print("\nThe spin resulted in = 0")


elif(a==38):
    
    print("\nThe spin resulted in = 00")

else:
    print("\nThe spin resulted in = ",a)

if(a>=1 and a<=36):

    if(a>=1 and a<=18):

        k="1 to 18"

        if(a==10 or a==11):

            if(a==10):
                eo="EVEN"

                s="BLACK"
            
            elif(a==11):
                eo="ODD"

                s="BLACK"
                

    
        if(a>=1 and a<=9):

            if(a%2==0):
                
                eo="EVEN"
                
                s="BLACK"
        
            else:

                eo="ODD"

                s="RED"
    
        elif(a>=12 and a<=18):

            if(a%2==0):

                eo="EVEN"

                s="RED"
        
            else:

                eo="ODD"

                s="BLACK"
    
    elif(a>=19 and a<=36):

        k="19 to 36"

        if(a>=19 and a<=27):

            if(a%2==0):
                
                eo="EVEN"

                s="BLACK"
            
            else:

                eo="ODD"

                s="RED"
        
        if(a==28 or a==29):

            if(a==28):
                
                eo="EVEN"

                s="BLACK"
            
            elif(a==29):
                
                eo="ODD"

                s="BLACK"
        
        if(a>=30 and a<=36):

            if(a%2==0):

                eo="EVEN"

                s="RED"

            else:

                eo="ODD"

                s="BLACK"

# Conditions for spin 37 and 38
if(a==37 or a==38):
    
    if(a==37):
        a='0'
        print(f"\nPay {a}\n")
    
    elif(a==38):
        a='00'
        print(f"\nPay {a}\n")
        
else:
    print(f"\nPay {a}\n\
Pay {s}\n\
Pay {eo}\n\
Pay {k}\n")

# Displaying the closing message after the spin
print("\nThanks for playing! Spin again to test your luck!\n")


