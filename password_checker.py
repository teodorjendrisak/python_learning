import getpass

COMMON_PASSWORDS = [
    "123456",
    "password",
    "123456789",
    "12345",
    "12345678",
    "qwerty",
    "111111",
    "123123",
    "abc123",
    "password1"
]

def get_password_issues(password):
    issues = []
    if not has_minimum_length(password):
        issues.append("Include at least 8 characters")
    if not has_upper_and_lower(password):
        issues.append("Include both uppercase and lowercase letters")
    if not has_digits(password):
        issues.append("Include number(s)")
    if not has_special_characters(password):
        issues.append("Include special character(s)")
    return issues

def has_minimum_length(password):
    return 8 <= len(password)

def has_upper_and_lower(password):
    has_upper = False
    has_lower = False

    for letter in password:
        if letter.isupper():
            has_upper = True
        if letter.islower():
            has_lower = True

    return has_upper and has_lower

def has_digits(password):
    for number in password:
        if number.isnumeric():
            return True
    return False

def has_special_characters(password):
    special_characters = "!@#$%^&*()-_=+"

    for letter in password:
        if letter in special_characters:
            return True
    return False

def main():
    password = getpass.getpass("Enter a password ")
    password_confirm = getpass.getpass("Confirm your password ")

    if password == password_confirm:
        if password in COMMON_PASSWORDS:
            print("The password is too common")
            return

        issues = get_password_issues(password)

        if not issues:
            print("Strong password")
        elif len(issues) == 1:
            print("Moderate password")
            for issue in issues:
                print(issue)
        else:
            print("Weak password")
            for issue in issues:
                print(issue)
    else:
        print("Passwords do not match")

if __name__ == "__main__":
    main()