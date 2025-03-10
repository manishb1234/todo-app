def strength(password):
    result = []
    if len(password) >= 8:
        result.append(True)
    else:
        result.append(False)

    #print(strength('acsssavfbfsbs'))

    result.append(False)
    for i in password:
        if i.isupper():
            result[1]=True

    result.append(False)
    for i in password:
        if i.isdigit():
            result[2]=True

    for i in result:
        if i==False:
            return "Weak Password"

    return "Strong Password"

print(strength("hellomoto124"))

"""
    Using flags
    
    def strength(password):
    has_upper = False   # Flag for uppercase letter
    has_digit = False   # Flag for digit

    if len(password) < 8:
        return "Weak Password"  # Early exit if length is insufficient

    for char in password:
        if char.isupper():
            has_upper = True  # If an uppercase letter is found, set flag to True
        elif char.isdigit():
            has_digit = True  # If a digit is found, set flag to True

        # If both flags are True, we can return early
        if has_upper and has_digit:
            return "Strong Password"

    return "Weak Password"
"""

def average(arg):
    sum1 = 0
    for i in arg:
        sum1 = sum1 + float(i)
    average_local = sum1 / float(len(arg))
    return average_local

print(average([10,20,30,40]))