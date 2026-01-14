'''Check IF a String Is Palindrome'''

# Defining a function to check if a given string is a palindrome
def is_palindrome(s):

    # Converting the string to lowercase and removing all spaces
    s=s.lower().replace(" ","")

    # Return True if the string is equal to its reverse, False otherwise
    return s==s[::-1]

# Printing a header to indicate the strings being checked
print("\nThe strings in code :-")

# Checking if the example strings are palindromes and printing the results
print("\nIs string 1 is a palindrome = ",is_palindrome("A man a plan a canal Panama"))
print(f"\nIs string 2 is a palindrome = {is_palindrome("Hello")}\n")