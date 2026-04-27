# fx number 1
def check_length(password, min_length=8):
    if len(password) >= min_length:
        return True
    return False

# print(f"{check_length(password)}")

# number 2    
def has_digit(password):
    hasDigit = False
    for char in password:
        if char.isdigit():
            hasDigit = True
            return hasDigit
    return False        
# print(f"{has_digit(password)}")

# fx 3            
def has_uppercase(password):
    hasUpper = False
    for char in password:
        if char.isupper():
            hasUpper = True
            return hasUpper
    return False
# print(f"{has_uppercase(password)}")

# fx 4
def has_lowercase(password):
    hasLower = False
    for char in password:
        if char.islower():
            hasLower = True
            return hasLower
    return False
        
# print(f"{has_lowercase(password)}")

# fx 5
def has_special_char(password):
    hasSpecial = False
    specialChars = '!@#$%^&*()<>?'
    for char in password:
        if char in specialChars:
            hasSpecial = True
            return hasSpecial
    return False
            
# print(f"{has_special_char(password)}")

# fx 6
def is_common_password(password):
    commonPass = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "monkey", "dragon", "master", "sunshine"]
    for common in commonPass:
        if common in password.lower():
            return True
    return False

# print(f"{is_common_password(password)}")

# fx 7
def calculate_strength_score(password):
    totalScore = 0
    if check_length(password, 12):
        totalScore += 3
    elif check_length(password, 8):
        totalScore += 2
    else:
        totalScore += 0
    if has_digit(password):
        totalScore += 2
    else:
        totalScore += 0
    if has_uppercase(password):
        totalScore += 1
    else:
        totalScore += 0
    if has_lowercase(password):
        totalScore += 1
    else:
        totalScore += 0
    if has_special_char(password):
        totalScore += 2
    else:
        totalScore += 0
    if is_common_password(password):
        totalScore -= 2  #(using a common password is weak and should be frowned upon)
    else:
        totalScore += 1 
    return totalScore
# print(f"{calculate_strength_score(password)}")

# fx 8

def get_strength_rating(score):
    if score < 4:
        return "Weak"
    elif score < 6:
        return "Medium"
    elif score < 8:
        return "Strong"
    elif score < 10:
        return "Excellent"
    else:
        return "Superior!!"
    
# fx 9

def analyze_password(password):
    # this is the main function that combines everything and returns a
    # dictionary
    score = calculate_strength_score(password)
    rating = get_strength_rating(score)
    
    passed = []
    failed = []
    
    if check_length(password, 8):
        passed.append("Length >= 8")
    else:
        failed.append("Length >= 8")
    
    if check_length(password, 12):
        passed.append("Length >= 12")
    else:
        failed.append("Length >= 12")
        
    if has_digit(password):
        passed.append("Has digit")
    else:
        failed.append("Has digit")
    
    if has_uppercase(password):
        passed.append("Has uppercase")
    else:
        failed.append("Has uppercase")
        
    if has_lowercase(password):
        passed.append("Has lowercase")
    else:
        failed.append("Has lowercase")
        
    if has_special_char(password):
        passed.append("Has special character")
    else:
        failed.append("Has special character")
    
    if not is_common_password(password):
        passed.append("Not common password")
    else:
        failed.append("Not common password")
    
    return {
        "password": password,
        "score": score,
        "rating": rating,
        "passed_checks": passed,
        "failed_checks": failed
    }
# print(f"Your password strength rating is {get_strength_rating(calculate_strength_score(password))}")
# all the test print statements should not be here since they are for
# testing and debugging and a Library doesn't have test statements