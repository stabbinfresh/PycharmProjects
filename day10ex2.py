total_value = input("Enter the total value: ")

value = input("Enter the value: ")

try:
    num_total_value = float(total_value)
    num_value = float(value)

    percent = round(num_value/num_total_value, 3) * 100
    print(f"That is {percent}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")