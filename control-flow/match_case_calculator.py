
  #prompt user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))    
#prompt for the type of opeartion
operation = input("Choose the operation (+, -, *, /):. ")
#Implement a Match Case statement that executes the chosen operation based on the user’s inpu
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Error: Can not divide by zero.")
    case _:
        print("Invalid operation selected. Please choose from +, -, *, /.")
