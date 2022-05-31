from ast import Expression

from jmespath import search


# Regulart Expression to search a capital then number then -
import re

def match(text):
        patterns = '^[A-Z][0-9]-'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

#Test case !
print(match("E3-"))

#Test Case 2:
print(match("e3-"))