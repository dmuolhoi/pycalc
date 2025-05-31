import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input():
    input1 = float(input("Input first number: "))
    input2 = float(input("Input second number: "))
    return input1, input2

def add(input1, input2):
    return input1 + input2

def subtract(input1, input2):
    return input1 - input2

def multiply(input1, input2):
    return input1 * input2

def divide(input1, input2):
    if input2 == 0:
        return "Error: Cannot divide by zero"
    return input1 / input2

# Exit commands stored here
exit_commands = ['exit', 'quit', 'q', 'bye', 'leave', 'close', 'x']

while True:
    clear()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("\n(You can also type: " + ", ".join(exit_commands) + ")")

    user_input = input("\nPick a number or command: ").strip().lower()

    # Exit if user types a known exit command or 5
    if user_input == '5' or user_input in exit_commands:
        print("\nExiting calculator. Goodbye!\n")
        break

    if user_input in ['1', '2', '3', '4']:
        clear()
        input1, input2 = get_input()

        if user_input == '1':
            result = add(input1, input2)
        elif user_input == '2':
            result = subtract(input1, input2)
        elif user_input == '3':
            result = multiply(input1, input2)
        elif user_input == '4':
            result = divide(input1, input2)

        print("\nResult:", result)
    else:
        # Catch anything else
        print("\nInvalid input. Please choose a number from 1 to 5, or type 'exit' to quit.")

    input("\nPress Enter to continue")