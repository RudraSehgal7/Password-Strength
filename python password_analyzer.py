import re

def analyze_password(password):
    # Define the criteria
    min_length = 12
    contains_letter = bool(re.search(r'[A-Za-z]', password))
    contains_number = bool(re.search(r'[0-9]', password))
    contains_symbol = bool(re.search(r'[@$!%*?&#]', password))

    # Check if password meets each requirement
    length_check = len(password) >= min_length
    all_criteria_met = length_check and contains_letter and contains_number and contains_symbol

    # Feedback messages
    if all_criteria_met:
        print("Awesome Work! Your password is strong.")
    else:
        print("Your password could be stronger. Consider the following suggestions:")
        if not length_check:
            print("- Use at least 12 characters.")
        if not contains_letter:
            print("- Include at least one letter (A-Z or a-z).")
        if not contains_number:
            print("- Include at least one number (0-9).")
        if not contains_symbol:
            print("- Include at least one special symbol (e.g., @, $, %, &, #, etc.).")

# Main function to run the password analyzer
def main():
    print("Welcome to the Password Analyzer!")
    password = input("Enter your password: ")
    analyze_password(password)

if __name__ == "__main__":
    main()
