def add(M, N):
   return M + N

def subtract(M, N):
   return M - N

def multiply(M, N):
   return M * N

def divide(M, N):
   return M / N

print("Please select the operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice: ")

var1 = int(input("Please enter the first number: "))
var2 = int(input("Please enter the second number: "))

if choice == 'a':
   print(var1, " + ", var2, " = ", add(var1, var2))

elif choice == 'b':
   print(var1, " - ", var2, " = ", subtract(var1, var2))

elif choice == 'c':
   print(num1, " * ", num2, " = ", multiply(num1, num2))

elif choice == 'd':
   print(var1, " / ", var2, " = ", divide(var1, var2))

else:
   print("This is an invalid input")
