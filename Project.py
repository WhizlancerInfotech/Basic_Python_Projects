import math

# Memory function to store and recall value
memory = None

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def calculator():
    global memory
    print("Simple Calculator with Advanced Features")
    while True:
        # Show available options
        print("\nSelect Operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Memory Store")
        print("8. Memory Recall")
        print("9. Exit")
        
        # Take input from user
        choice = input("Enter choice (1-9): ")

        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            # Validate user input for numbers
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            # Perform selected operation
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {power(num1, num2)}")
        
        elif choice == '6':
            try:
                num = float(input("Enter the number: "))
                print(f"Result: {sqrt(num)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '7':
            memory = float(input("Enter number to store in memory: "))
            print(f"Stored {memory} in memory.")
        
        elif choice == '8':
            if memory is not None:
                print(f"Recalled value from memory: {memory}")
            else:
                print("Memory is empty.")

        else:
            print("Invalid input. Please choose a valid option.")

# Run the calculator
calculator()
