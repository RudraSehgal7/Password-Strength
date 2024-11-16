# -*- coding: utf-8 -*-

import re
from zxcvbn import zxcvbn
import sys

def analyze_password_strength(password):
    try:
        result = zxcvbn(password)
        return {
            "score": result['score'],
            "feedback": result['feedback']
        }
    except Exception as e:
        return {"error": str(e)}

def validate_password_requirements(password):
    errors = []
    if not re.search(r'[a-zA-Z]', password):
        errors.append("Password must contain at least one alphanumeric character.")
    if not re.search(r'\d', password):
        errors.append("Password must contain at least one number.")
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        errors.append("Password must contain at least one special character.")
    return errors

def main():
    while True:
        password = input("\nEnter a password: ")
        if password.lower() == 'exit':
            break

        validation_errors = validate_password_requirements(password)
        if validation_errors:
            for error in validation_errors:
                print(f" - {error}")
            continue

        analysis = analyze_password_strength(password)

        if "error" in analysis:
            print(f"Error analyzing password: {analysis['error']}")
        else:
            score = analysis['score']
            if score == 4:
                sys.exit()

if __name__ == "__main__":
    main()
