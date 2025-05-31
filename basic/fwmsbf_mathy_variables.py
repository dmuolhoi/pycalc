import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_xy():
    x = float(input("num1: "))
    y = float(input("num2: "))
    return x, y

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "cannot divide by zero"
    return x / y

# Define custom exit commands
q = ['5', 'q', 'x']

while True:
    clear()
    print("+")
    print("-")
    print("*")
    print("÷")
    print("x")
    
    u = input("pick a number or command: ").strip().lower()
    
    # Exit if user input matches an exit command
    if u in q:
        print("exit.")
        break
    
    elif u == '1':
        clear()
        x, y = get_xy()
        print("result:", add(x, y))
    
    elif u == '2':
        clear()
        x, y = get_xy()
        print("result:", minus(x, y))
    
    elif u == '3':
        clear()
        x, y = get_xy()
        print("result:", multiply(x, y))
    
    elif u == '4':
        clear()
        x, y = get_xy()
        print("result:", divide(x, y))
    
    else:
        print("Input invalid")

    input("\nenter to continue")