while True:
    user_action = input("Throw the coin and enter head or tail here: ? ")
    user_action = user_action.strip() + "\n"

    with open("coin_flips.txt", "r") as file:
        flips = file.readlines()

    flips.append(user_action)

    with open("coin_flips.txt", "w") as file:
        file.writelines(flips)

    heads = flips.count("head\n")
    count = len(flips)
    percent = round(heads/count, 3) * 100
    message = f"Heads: {percent}%"
    print(message)