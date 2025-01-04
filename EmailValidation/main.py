"""
Email Validation Program

This program validates email addresses to ensure they follow basic criteria:
- The email contains an '@' symbol.
- The email ends with one of the allowed domains: '@gmail.com', '@rediffmail.com', or '@yahoomail.com'.
- The username portion of the email (before '@') consists of alphanumeric characters.

Developer: Mohit Kolte
Date: January 5, 2025
Python Version: 3.12
"""

def input_email():
    return input("Enter the email address: ")

def main():
    email = input_email()
    if '@' in email:
        try:
            if email.endswith('@gmail.com') or email.endswith('@rediffmail.com') or email.endswith('@yahoomail.com'):
                username = email.split[0]
                if username.isalnum():
                    print("Email validated.")
        except Exception as e:
            print(f"Invalid email {e}")
    else:
        print("Invalid Email")

if __name__ == "__main__":
    main()