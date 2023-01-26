names = input("Enter names separated by commas (no spaces): ")

def get_number_names(user_input):
    names_local = user_input.split(',')
    return len(names_local)

print(get_number_names(names))