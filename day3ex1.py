while True:
    user_action = input("Enter the country you are from: ")
    user_action = user_action.lower()

    match user_action:
        case 'usa':
            print("Hello")
        case 'india':
            print("Namaste")
        case 'germany':
            print("Hallo")
    break