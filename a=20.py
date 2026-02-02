num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
op = input("Enter operator (+, -, *, /): ")

num1 = float(num1)
num2 = float(num2)

if op == '+':
    print("Result:", num1, "+", num2, "=", num1 + num2)
elif op == '-':
    print("Result:", num1, "-", num2, "=", num1 - num2)
elif op == '*':
    print("Result:", num1, "*", num2, "=", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result:", num1, "/", num2, "=", num1 / num2)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator")