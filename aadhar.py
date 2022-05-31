#! usr/bin/python3
# promt the user to enter aadhar number in the format dddd-dddd-dddd  and check if it is valid or not
#Am using Regular Expressions!

# prompt user 
number=input("Enter Aadhar Number in the format: 'dddd-dddd-dddd':  ")
from ast import Not
from asyncio.windows_events import NULL
import re
#Creating A match
aadharNumber=re.compile(r'\d{4}-\d{4}-\d{4}')
#Searching
mo=aadharNumber.search(number)
#Validation
try:
    mo.group
    print("Aadhar Number Found!:", mo.group())
except:
    print("Invalid Aadhar Number!")

#END
#Rish!