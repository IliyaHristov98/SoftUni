def password_validation(password):
    long_enough = 6 <= len(password) <= 10
    letter_and_digits = password.isalnum()
    digit_count = sum(1 for i in password if i.isdigit())
    if not long_enough:
        print("Password must be between 6 and 10 characters")

    if not letter_and_digits:
        print("Password must consist only of letters and digits")

    if digit_count < 2:
        print("Password must have at least 2 digits")

    if long_enough and letter_and_digits and digit_count >= 2:
        return "Password is valid"
    else:
        return ""


input_password = input()
print(password_validation(input_password))