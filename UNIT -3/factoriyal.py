# Write a program to input a number and display Factorial of that number. For example, Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120.
# Roll Number : 92400527141 Name : Gaurav

n = int(input("Enter the number :"))

fact = 1
for i in range (1,n+1):
    fact = fact * i
print(f"FACTORIYAL of {n} is {fact}")
