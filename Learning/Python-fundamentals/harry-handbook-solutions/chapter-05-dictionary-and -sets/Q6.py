'''Q6:-Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique'''

"""
Summary :- In this program we will create an dictionary key as their names and value as their favourite language.
"""

# taking input from the user to enter their favourite language
l1=input("mr anubhav enter your favourite language as value for dictionary :-  ")
l2=input("mr krishna enter your favourite language as value for dictionary :-  ")
l3=input("miss radha enter your favourite language as value for dictionary :-  ")
l4=input("miss bhavani enter your favourite language as value for dictionary :-  ")

dic={}# created an empty dictionary

# dictionary is in curly bracket{}, set is in curly bracket{} but an empty set is created using set() , 
# list is in braces[], tuple is in parentheses()

#adding the key value pair to the dictionary using update() function

"""what update function does:- update() function is used to add the key value pair to the dictionary 
or to update the value of the existing key in the dictionary
syntax of update function:- dictionary_name.update({key:value})"""

dic.update({"anubhav":l1})
dic.update({"krishna":l2})
dic.update({"radha":l3})
dic.update({"bhavani":l4})

# displaying the dictionary to the user
print(dic)