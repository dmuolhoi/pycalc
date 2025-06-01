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

# Exit commands
exit_commands = ['5', 'exit', 'quit', 'q', 'x', 'bye']

while True:
    clear()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    user_input = input("Pick a number or command: ").strip().lower()
    
    if user_input in exit_commands:
        print("Exiting calculator.")
        break

    elif user_input == '1':
        clear()
        input1, input2 = get_input()
        print("Result:", add(input1, input2))

    elif user_input == '2':
        clear()
        input1, input2 = get_input()
        print("Result:", subtract(input1, input2))

    elif user_input == '3':
        clear()
        input1, input2 = get_input()
        print("Result:", multiply(input1, input2))

    elif user_input == '4':
        clear()
        input1, input2 = get_input()
        print("Result:", divide(input1, input2))

    else:
        print("Invalid input. Please enter 1–5 or a valid command like 'quit'.")

    input("\nPress Enter to continue ")