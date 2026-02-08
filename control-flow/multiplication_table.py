#prompt the user for the number1 and 2
num = int(input("Enter the number: "))
#For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
#Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.
for i in range (1 ,11):
    results = num * int(i)

    print (f"{num} * {i} = {results}")