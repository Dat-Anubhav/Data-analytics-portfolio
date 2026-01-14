'''Q15:- Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. 
Convert the dictionary to a JSON string and print it.'''
# Importing json module
import json

# Creating a dictionary to represent a book's details
book={
"Title" : "A BRIEF HISTORY OF TIME",
"Author" : "Stephen Hawking",
"Year" : 1988,
"Genre" : "Popular science" 
}

# Displaying the dictionary to the user for reference
print("\nA dictionary representing a book")

print(f"{book} {type(book)}")

# Convert the dictionary to a JSON string
book_j= json.dumps(book)

print("\nConverting the dictionary into a JSON string")

# Printing the JSON string
print(f"{book_j} {type(book_j)}\n")

'''JSON (JavaScript Object Notation) is a way to write and share data using text that looks 
like a Python dictionary, with curly braces, keys, and values. It is used when sending data 
between different programs, websites, or computers because it is easy for both people and 
computers to read and write'''