def get_todos(filepath="todos.txt"):
    """Get the items in the file as a list """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write the given list to a file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


solid_temp = 0

boiling_temp = 100


def get_state(temperature):
    """a function that takes the given Celsius
     temperature and returns whether it is
     solid, liquid, or gas"""

    if temperature <= solid_temp:
        return "Solid"
    elif solid_temp < temperature < boiling_temp:
        return "Liquid"
    else:
        return "Gas"
