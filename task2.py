# Simple Calculator

name = input("Enter your name: ")
age = input("Enter your age: ")

print("\nHello", name)
print("You are", age, "years old.")

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults")
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0:
    print("Division =", num1 / num2)
else:
    print("Cannot divide by zero")

if num1 > num2:
    print(num1, "is greater")
elif num2 > num1:
    print(num2, "is greater")
else:
    print("Both numbers are equal")

both_positive = num1 > 0 and num2 > 0
print("Both numbers are positive:", both_positive)