# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers and find the largest
if num1 > num2:
    largest = num1
else:
    largest = num2

# Print the result
print(f"The largest of {num1} and {num2} is: {largest}")
