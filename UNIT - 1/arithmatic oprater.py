# Write a program to input Two Number 
# Roll Number : 92400527141 Name : Gaurav

a = float(input("Enter first Number : " ))
b = float(input("Enter second Number : " ))
op = input("Enter Opreater ( +,-,,*,/):")

if op == "+":
    print("Result = " , a + b)
elif op == "-":
    print("Result = " , a - b)
elif op == "-":
    print("Result = " , a * b)
elif op == "-":
    print("Result = " , a / b)
else :
    print("Invalid Opreater")

