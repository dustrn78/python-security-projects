# Password Strength Checker

A Python tool that evaluates password strength based on multiple security criteria.

##  Purpose

This tool helps users create stronger passwords by analyzing them against common security requirements and providing actionable feedback.

##  Features

-  **Length validation** - Checks for minimum 8 characters (excellent at 12+)
-  **Character variety** - Ensures passwords contain both letters and numbers
-  **Case sensitivity** - Verifies mix of uppercase and lowercase letters
-  **Scoring system** - Rates passwords from 0-6 points
-  **Detailed feedback** - Provides specific improvement suggestions

##  How It Works

The checker evaluates passwords across three criteria:

1. **Length** (0-3 points)
   - 12+ characters: Excellent (3 points)
   - 8-11 characters: Good (2 points)
   - <8 characters: Weak (0 points)

2. **Character types** (0-2 points)
   - Contains letters AND numbers: 2 points
   - Missing either: 0 points

3. **Mixed case** (0-1 point)
   - Has both uppercase AND lowercase: 1 point
   - All same case: 0 points

### Rating System

- **Strong** (5-6 points) - Meets all security requirements
- **Medium** (3-4 points) - Meets some requirements  
- **Weak** (0-2 points) - Needs significant improvement

##  Usage

```bash
python password_checker.py
```

Then enter a password when prompted.

## Example Output


=== PASSWORD STRENGTH CHECKER ===

Enter a password to check: TestPassword2025

--- Analysis Results ---
Excellent length (12+ characters)
Contains letters and numbers
Has mixed case

Strength Score: 6/6
Overall Rating: Strong


## What I Learned

Building this project taught me:

- **String methods** - `isalpha()`, `isdigit()`, `isupper()`, `islower()`, `len()`
- **For loops** - Iterating through each character in a string
- **Conditional logic** - Using if/elif/else to check multiple conditions
- **Lists** - Using `append()` to build feedback messages
- **User input** - Getting and validating user input with `input()`
- **F-strings** - Modern string formatting for clean output

##  Future Enhancements

Planned improvements for v2.0:

- [ ] Check for special characters (@, #, $, %, etc.)
- [ ] Detect common weak passwords (password123, qwerty, etc.)
- [ ] Identify sequential patterns (123, abc)
- [ ] Check against leaked password databases
- [ ] Add entropy calculation
- [ ] Provide password generation suggestions

##  Technologies

- **Python 3.x**
- Built-in string methods (no external dependencies)

##  Security Note

This is an educational project. For production use, passwords should:
- Never be stored in plain text
- Be hashed with bcrypt, Argon2, or similar
- Follow OWASP password guidelines
- Be checked against known breach databases (HaveIBeenPwned API)

---

*Created as part of Unit 1: Python Fundamentals course*
*December 2025*
