def add(num1, num2):
   return num1 + num2

def subtract(num1, num2):
   return num1 - num2

def multiply(num1, num2):
   return num1 * num2

def divide(num1, num2):
   return num1 / num2

print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice: ")

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if choice == 'a':
   print(num1, " + ", num2, " = ", add(num1, num2))

elif choice == 'b':
   print(num1, " - ", num2, " = ", subtract(num1, num2))

elif choice == 'c':
   print(num1, " * ", num2, " = ", multiply(num1, num2))

elif choice == 'd':
   print(num1, " / ", num2, " = ", divide(num1, num2))

else:
   print("This is an invalid input")
