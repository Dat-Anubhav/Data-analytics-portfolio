'''Q1:- Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!'''

"""
Summary :- In this program we will create a dictionary of Hindi words with values as their English.
"""

# dictionary is a collection which is unordered, changeable and indexed.
# creating a dictionary of hindi words with values as their english translation.

# hdic is the name of the dictionary
hdic={"khush":"happy",
      "sad":"udaass",
      "gussa":"anger",
      "jalan":"jealousy",
      "kaam":"sex",
      "madhu":"sweet",
      "madira":"wine"}
# displaying the hindi words to the user
print(hdic.keys())

# taking input from the user to look up the translation of the hindi words.
l=input("please enter the word to know its translation in english")

# getting the value of the key entered by the user and displaying its value 
# corresponding to its english translation
print(hdic.get(l))