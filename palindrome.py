def reverse(number): 
    return int(str(number)[::-1]) 
  
def isPalindrome(number): 
    if number == reverse(number):
        print("True")
    else:
        print("False")

# Test case 1 expected output is ::True
isPalindrome(4444)
# Test case 2 expected output is False
isPalindrome(9073)
    
