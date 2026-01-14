'''Q4 :- Write a python program to print the contents of a directory using the os module.
 Search online for the function which does that
 
 Q5: Add comments in the Q4 program. (Done below)'''

import os

# You can either specify a path or use the current directory '.'
directory_path = '.'

# Call os.listdir() to get the list of files and directories
contents = os.listdir(directory_path)

# Print each item in the contents list
print(f"Contents of '{directory_path}':") 
# Here, an f-string is used to include the value of a variable (directory_path) inside the string.

for item in contents:
    print(item)
# chapter 1 test has ended here. Q5 (add comments in the Q4 program) has also been completed in this program.  