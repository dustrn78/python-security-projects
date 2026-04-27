# Password Analyzer Library

A reusable Python library for password strength analysis.

## What It Does

Provides 9 functions for comprehensive password validation:
- Length checking (with customizable minimum)
- Digit detection
- Uppercase/lowercase detection
- Special character detection
- Common password checking
- Strength scoring (0-10)
- Strength rating (Weak/Medium/Strong/Excellent/Superior)
- Complete password analysis with detailed results

## Usage

```python
import PasswordAnalyzerLibrary as pal

# Analyze a password
result = pal.analyze_password("Test123!")

print(f"Score: {result['score']}/10")
print(f"Rating: {result['rating']}")
print(f"Passed: {result['passed_checks']}")
print(f"Failed: {result['failed_checks']}")
```

## Functions

- `check_length(password, min_length=8)` - Check password length
- `has_digit(password)` - Check for digits
- `has_uppercase(password)` - Check for uppercase letters
- `has_lowercase(password)` - Check for lowercase letters
- `has_special_char(password)` - Check for special characters
- `is_common_password(password)` - Check against common weak passwords
- `calculate_strength_score(password)` - Calculate score out of 10
- `get_strength_rating(score)` - Get rating from score
- `analyze_password(password)` - Complete analysis (main function)

## Key Concepts Learned

- Function modularity and reusability
- Default parameters
- Functions calling other functions
- Returning dictionaries
- Building Python libraries
- Importing and using modules

## Unit

**Unit 3: Functions** - Final Project
