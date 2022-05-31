#Password Validator Using Python

password=input("Enter your Password: ")
# validation:
# 8chars
# Letter and digits
# atleast 2 digits 


def validate_password(password):
    if len(password) < 8:
        return False
    if not all(char.isdigit() or char.isalpha() for char in password):
        return False
    if sum(char.isdigit() for char in password) < 2:
        return False
    return True
print(validate_password(password))
