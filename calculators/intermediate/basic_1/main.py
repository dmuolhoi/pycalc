from calculator import add, subtract, multiply, divide
from input_utils import get_number
from menu import show_menu

exit_commands = ['5', 'exit', 'quit', 'q']

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip().lower()

        if choice in exit_commands:
            print("Exiting calculator.")
            break

        if choice in ['1', '2', '3', '4']:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")
            if choice == '1':
                print("Result:", add(a, b))
            elif choice == '2':
                print("Result:", subtract(a, b))
            elif choice == '3':
                print("Result:", multiply(a, b))
            elif choice == '4':
                print("Result:", divide(a, b))
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
