# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: The result of the operation, or a message if division by zero occurs
                      or if an invalid operation is provided.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1/num2
        else:
             "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Example usage:
if __name__ == "__main__":
    print(perform_operation(10, 5, "add"))       # Output: 15
    print(perform_operation(10, 5, "subtract"))  # Output: 5
    print(perform_operation(10, 5, "multiply"))  # Output: 50
    print(perform_operation(10, 5, "divide"))    # Output: 2.0
    print(perform_operation(10, 0, "divide"))    # Output: Error: Division by zero
    print(perform_operation(10, 5, "modulus"))   # Output: Error: Invalid operation
