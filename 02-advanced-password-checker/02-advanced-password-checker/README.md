# Advanced Password Strength Checker v2.0

A comprehensive Python tool that analyzes password security based on multiple criteria and provides detailed feedback for improvement.

## Features

- **Length Validation** - Scores passwords based on length (8+ minimum, 12+ excellent)
- **Character Variety** - Ensures passwords contain both letters and numbers
- **Case Sensitivity** - Verifies mix of uppercase and lowercase letters
- **Special Characters** - Checks for symbols (!@#$%^&*)
- **Weak Password Detection** - Identifies common weak passwords and patterns
- **Sequential Pattern Detection** - Detects sequences like "123" or "abc"
- **Smart Scoring System** - 10-point scale with detailed ratings
- **Interactive Loop** - Check multiple passwords in one session

## How It Works

The checker evaluates passwords across six security criteria:

### Scoring Breakdown

**Total: 10 points possible**

1. **Length** (0-3 points)
   - 12+ characters: 3 points
   - 8-11 characters: 2 points
   - Less than 8: 0 points

2. **Character Variety** (0-2 points)
   - Contains letters AND numbers: 2 points
   - Missing either: 0 points

3. **Mixed Case** (0-1 point)
   - Has uppercase AND lowercase: 1 point
   - All same case: 0 points

4. **Special Characters** (0-2 points)
   - Contains special characters: 2 points
   - No special characters: 0 points

5. **Weak Password Check** (0-1 point, with penalty)
   - Not a common weak password: 1 point
   - Contains weak pattern: -2 points (penalty)

6. **Sequential Patterns** (0-1 point)
   - No sequential patterns: 1 point
   - Contains sequences (123, abc): 0 points

### Rating System

- **9-10 points:** Excellent - Very strong password
- **7-8 points:** Strong - Good password
- **5-6 points:** Medium - Acceptable but could be stronger
- **0-4 points:** Weak - Needs significant improvement

## Usage

```bash
python advancePasswordCheckerProject.py
```

Then enter a password when prompted.

## Example Output

```
=== ADVANCED PASSWORD STRENGTH CHECKER ===

Enter a password to check (or 'quit' to exit): MySecure!Pass2025

--- ANALYSIS RESULTS ---
Excellent length at 17 characters.
Your password has both letters and numbers
Password has both upper and lower case letters
Good job not using a common or weak password!
Your password contains special characters
No sequential patterns detected

Strength Score: 10/10
Overall Rating: EXCELLENT
This password is very strong!

Check another password? (yes/no):
```

## Security Checks Explained

### Weak Password Detection

Checks against common weak passwords including:
- password
- 123456
- qwerty
- admin
- letmein
- welcome
- dragon
- master
- sunshine

Also detects if these patterns appear anywhere within the password (e.g., "MyPassword123" contains "password").

### Sequential Pattern Detection

Identifies sequential patterns that make passwords easier to crack:
- **Number sequences:** 123, 234, 987, 321
- **Letter sequences:** abc, bcd, xyz (case-insensitive)

Checks both ascending and descending sequences.

## What I Learned

Building this project taught me:

**Python Concepts:**
- While loops for interactive programs
- For loops with range indexing
- String manipulation and methods (`.isalpha()`, `.isdigit()`, `.isupper()`, `.islower()`)
- List operations (`.append()`)
- The `in` operator for substring and list checking
- Break and continue statements
- ASCII value comparison with `ord()`
- Working with boolean flags

**Security Concepts:**
- Password strength requirements
- Common weak password patterns
- Sequential pattern vulnerabilities
- Multi-factor password scoring
- User feedback for security improvements

**Programming Patterns:**
- Search and flag pattern
- Input validation loops
- Multi-criteria scoring systems
- Interactive command-line interfaces

## Future Enhancements

Potential improvements for v3.0:

- [ ] Check against breached password databases (HaveIBeenPwned API)
- [ ] Calculate password entropy
- [ ] Detect keyboard patterns (qwerty, asdf)
- [ ] Check for repeated characters (aaa, 111)
- [ ] Dictionary word detection
- [ ] Password generation with custom requirements
- [ ] Save/load custom weak password lists
- [ ] Export results to file
- [ ] GUI interface

## Technologies

- **Python 3.x**
- Built-in string methods (no external dependencies)

## Project Context

Created as the final project for Unit 2 of a Python security fundamentals course, demonstrating:
- Loop mastery (while and for loops)
- Complex conditional logic
- String processing
- User interaction design
- Security-focused development

## Security Note

This is an educational tool for learning password security principles. For production use:
- Passwords should never be stored in plain text
- Use bcrypt, Argon2, or similar hashing algorithms
- Follow OWASP password guidelines
- Implement rate limiting to prevent brute force attacks
- Consider using established password libraries for real applications

---

**Created by:** Dustin Lidster  
**Date:** January 2025  
**Course:** Unit 2 - Python Fundamentals with Security Focus
