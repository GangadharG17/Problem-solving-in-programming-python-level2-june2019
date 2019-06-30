
def PhoneNumberValidate(number):
    pattern = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}|^[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern,str(number)):
        return True
    return False

def emailValidator(email):
    pattern = '^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z]@[a-z]{3,18}[.][a-z][2-4]$'
    if re.match(pattern,str(email)):
        return True
    else:
    return False
        