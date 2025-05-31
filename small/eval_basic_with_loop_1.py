while True:
    user_input = input("Enter expression (or type 'exit' to quit): ").strip().lower()

    if user_input in ['exit', 'quit', 'q']:
        print("Goodbye!")
        break

    try:
        result = eval(user_input)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)