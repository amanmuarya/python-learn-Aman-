# Definition:
# Keywords in Python are reserved words that have predefined meanings and are used to define the syntax and structure of Python programs. They cannot be used as identifiers such as variable, function, or class names.

import keyword 
print(keyword.kwlist)
# display the complete list of keywords using the keyword module

# if = 10          #  Error because 'if' is a keyword
# if_value = 10      # Valid