password = input("Enter a new password: ")


def password_check(password_arg):
    result = {}

    if len(password_arg) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password_arg:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    uppercase = False
    for i in password_arg:
        if i.isupper():
            uppercase = True

    result["uppercase"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


print(password_check(password))