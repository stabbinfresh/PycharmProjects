password = input("Enter a new password: ")

if len(password) > 7:
    print("Great password!")
elif len(password) == 7:
    print("Password is OK, but not too strong.")
else:
    print("Your password is weak.")
