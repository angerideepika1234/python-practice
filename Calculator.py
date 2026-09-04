def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error"
    else:
        return a / b
def power(a, b):
    return a ** b
print("----- Calculator App -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
n = int(input("Select an option: "))
if n == 1:
    print(addition(num1, num2))
elif n == 2:
    print(subtraction(num1, num2))
elif n == 3:
    print(multiplication(num1, num2))
elif n == 4:
    print(division(num1, num2))
elif n == 5:
    print(power(num1, num2))
else:
    print("Invalid")