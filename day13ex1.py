birth_year = int(input("What is your year of birth? "))

def user_age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return age

print(user_age(birth_year))