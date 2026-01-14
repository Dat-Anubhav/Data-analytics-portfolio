'''Q5:- Write a program that prints all the numbers from 1 to 10 except 5 using a for loop and continue statement.'''

for i in range(1,11,1):

    if(i==5):
        continue # When the value of i reaches 5, the continue statement will bypass it.
    print(i)