while True:
    # Get first input
    raw1 = input("Enter first number (or /exit): ")
    if raw1 == "/exit":
        print("Goodbye!")
        break

    # Get second input
    raw2 = input("Enter second number (or /exit): ")
    if raw2 == "/exit":
        print("Goodbye!")
        break

    # Try converting to float
    try:
        num1 = float(raw1)
        num2 = float(raw2)
    except ValueError:
        print("Please enter valid numbers.")
        continue

    # Perform addition
    result = num1 + num2
    print("Result:", result) 