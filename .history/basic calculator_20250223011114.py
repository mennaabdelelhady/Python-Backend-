num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator: ")

if operator == "+":
    print('the addition is',num1 + num2)
elif operator == "-":
    print('the subtraction',num1 - num2)
elif operator == "*":
    print('the multiplication',num1 * num2)
elif operator == "/":
    print('the division is',num1 / num2)
else:
    print("Invalid operator")
