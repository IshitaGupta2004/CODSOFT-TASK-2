def print_boxed(message):
    # Print the message in a box
    border = '+' + '-' * (len(message) + 2) + '+'
    print(border)
    print(f"| {message} |")
    print(border)

def calculator():
    print_boxed("Welcome to the Simple Calculator")
    
    # Getting two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Input: Get the operation choice from the user
    print_boxed("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Select any simple operation (1/2/3/4): ")

    # Perform the calculation based on the operation chosen
    if operation == '1':
        result = num1 + num2
        print_boxed(f"The result of adding {num1} and {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print_boxed(f"The result of {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print_boxed(f"The result of multiplying {num1} with {num2} = {result}")
    elif operation == '4':
        if num2 != 0:                     # Check for division by zero
            result = num1 / num2
            print_boxed(f"The result of {num1} / {num2} = {result}")
        else:
            print_boxed("Error: Division by zero is not allowed.")
    else:
        print_boxed("Invalid operation selected.")

# Run the calculator function
calculator()
