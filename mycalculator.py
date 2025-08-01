# Basic Calculator Program

# Ask the user for the first number
num1 = float(input("Hello! Please enter the first number: "))

# Ask the user for the second number
num2 = float(input("Now enter the second number: "))

# Ask the user for the operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation based on the selected operation
if operation == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: You can't divide by zero.")
else:
    print("Invalid operation. Please choose one of the following: +, -, *, or /.")

# Optional: Wait for user before closing (for some environments like Windows console)
input("👋 Press Enter to exit the calculator...")
