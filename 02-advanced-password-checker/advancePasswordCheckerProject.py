print("=== ADVANCED PASSWORD STRENGTH CHECKER ===\n")

specialChars = "!@#$%^&*"

keepChecking = True
while keepChecking:
    password = input("Enter a password to check (or 'quit' to exit): ")
    
    if password.lower() == "quit":
        print("Goodbye!")
        break
    
    # Initialize scoring
    score = 0
    feedback = []
    
    # Check 1: Length (0-3 points)
    length = len(password)
    if length >= 12:
        score += 3
        feedback.append(f"Excellent length at {length} characters.")
    elif length >= 8:
        score += 2
        feedback.append(f"Good length at {length} characters.")
    else:
        feedback.append(f"Too short! Your password has {length} characters. \nIt needs to be at least 8 characters long or more")
    
    # Check 2: Letters AND numbers (0-2 points)
    hasLetter = False
    hasNumber = False
    
    for char in password:
        if char.isalpha():
            hasLetter = True
        if char.isdigit():
            hasNumber = True
            
    if hasLetter and hasNumber:
        score += 2
        feedback.append("Your password has both letters and numbers")
    else:
        if not hasLetter:
            feedback.append("No letters detected in password")
        if not hasNumber:
            feedback.append("No numbers detected in password")
    
    # Check 3: Mixed case (0-1 point)
    hasUpper = False
    hasLower = False
    
    for char in password:
        if char.isupper():
            hasUpper = True
        if char.islower():
            hasLower = True
    
    if hasUpper and hasLower:
        score += 1
        feedback.append("Password has both upper and lower case letters")
    else:
        feedback.append("Your password is all the same case lettering. Might want to mix them up a bit!")
    
    # Check 4: Does password contain weak password patterns? (0-1pts)
    commonWeakPasswords = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "dragon", "master", "sunshine"]
    
    containsWeak = False
    for weakPass in commonWeakPasswords:
        if weakPass in password.lower():
            containsWeak = True
            break
    
    # FIXED: These checks are OUTSIDE the for loop
    if containsWeak:
        feedback.append("Doh!! Using that password is like leaving your front door wide open inviting hackers on in!!")
        score -= 2
    else:
        score += 1
        feedback.append("Good job not using a common or weak password!")
    
    # Check 5: Does password contain special chars? (0-2 points)
    hasSpecial = False
    
    for char in password:
        if char in specialChars:
            hasSpecial = True
            break
    
    if hasSpecial:
        score += 2
        feedback.append("Your password contains special characters")
    else:
        feedback.append("No special characters in password! (try adding !@#$%^&*)")
    
    # Check 6: Sequential patterns (0-1 point)
    hasSequence = False
    
    for i in range(len(password) - 2):
        char1 = password[i]
        char2 = password[i + 1]
        char3 = password[i + 2]
        
        # Check if all 3 are digits
        if char1.isdigit() and char2.isdigit() and char3.isdigit():
            # Ascending (123, 234, etc.)
            if int(char2) == int(char1) + 1 and int(char3) == int(char2) + 1:
                hasSequence = True
                feedback.append(f"Contains number sequence: {char1}{char2}{char3}")
                break
            # Descending (321, 987, etc.)
            if int(char2) == int(char1) - 1 and int(char3) == int(char2) - 1:
                hasSequence = True
                feedback.append(f"Contains number sequence: {char1}{char2}{char3}")
                break
        
        # Check if all 3 are letters
        if char1.isalpha() and char2.isalpha() and char3.isalpha():
            if ord(char2.lower()) == ord(char1.lower()) + 1 and ord(char3.lower()) == ord(char2.lower()) + 1:
                hasSequence = True
                feedback.append(f"Contains letter sequence: {char1}{char2}{char3}")
                break
    
    if not hasSequence:
        score += 1
        feedback.append("No sequential patterns detected")
    
    # Display results
    print("\n--- ANALYSIS RESULTS ---")
    for item in feedback:
        print(item)
    
    print(f"\nStrength Score: {score}/10")
    
    if score >= 9:
        print("Overall Rating: EXCELLENT!")
        print("This password is very strong!")
    elif score >= 7:
        print("Overall Rating: STRONG")
        print("This password is good.")
    elif score >= 5:
        print("Overall Rating: MEDIUM")
        print("This password is acceptable but could be stronger.")
    else:
        print("Overall Rating: WEAK")
        print("This password needs improvement!")
    
    print()
    another = input("Check another password? (yes/no): ")
    
    if another.lower() not in ["yes", "y"]:
        print("\nGoodbye!")
        keepChecking = False

print("\nThank you for using Password Strength Checker v2.0!")

