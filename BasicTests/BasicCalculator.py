# Simple calculator project with basic operations

# Function to add two numbers
def addition(x, y):
    return x + y  # Return the sum of x and y

# Function to subtract one number from another
def subtraction(x, y):
    return x - y  # Return the difference between x and y

# Function to multiply two numbers
def multiplication(x, y):
    return x * y  # Return the product of x and y

# Function to divide one number by another
def division(x, y):
    if y != 0:  # Check if the divisor is not zero
        return x / y  # Return the quotient of x divided by y
    else:  # Handle division by zero
        return "Invalid value!"  # Return an error message

# Function to execute the basic calculator operations
def basic_calculator():
    # Prompt the user to enter two numbers
    x = float(input("Please enter the first number: "))
    y = float(input("Please enter the second number: "))

    # Prompt the user to select an arithmetic operation
    operation = input("Please enter the operation (+, -, *, /): ")

    # Check which operation to perform and call the corresponding function
    if operation == "+":
        print("Result: ", addition(x, y))  # Perform addition
    elif operation == "-":
        print("Result: ", subtraction(x, y))  # Perform subtraction
    elif operation == "*":
        print("Result: ", multiplication(x, y))  # Perform multiplication
    elif operation == "/":
        print("Result: ", division(x, y))  # Perform division
    else:
        print("Invalid operation!")  # Handle invalid operation input

# Execute the calculator function
basic_calculator()  # Call the basic_calculator function to run the calculator
